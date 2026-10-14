"""The networking map: one block of HTML and one of CSS, written into the
poster between marker comments, so it can be rebuilt after the words change.
The words are kept in planning/networking-map.md; this is the shape they
take. Run it from anywhere; with --preview <file> it also writes a standalone
page for looking at the map on its own."""
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
TEMPLATE = HERE / "app.template.html"
ARROW = chr(0x2193)
DOT = chr(0xB7)

CSS = """
/* The networking map: one picture of where the networking questions live.
   Boxes two across at any width, so a phone gets the same shape as a desk. */
.netmap { margin: 4px 0 0; }
.netmap *, .netmap *::before { box-sizing: border-box; }
.netmap .lede { font-size: 0.86rem; margin: 0 0 8px; }
.nm-row { display: flex; flex-wrap: wrap; gap: 6px; align-items: stretch; }
.nm-row > * { flex: 1 1 140px; min-width: 0; }
.nm-box { border: 1px solid var(--rule); border-radius: 8px; background: var(--surface);
          padding: 6px 8px; }
.nm-box h4 { margin: 0 0 1px; font-size: 0.9rem; font-weight: 600; line-height: 1.3; }
.nm-box p { margin: 0; font-size: 0.8rem; color: var(--ink-2); line-height: 1.45; }
.nm-box .pick { color: var(--magenta); font-weight: 600; }
.nm-box.edge { border-left: 4px solid var(--cyan); }
.nm-box.hub  { border-left: 4px solid var(--magenta); }
.nm-zone { border: 2px dashed var(--rule); border-radius: 10px; padding: 7px; margin: 0; }
.nm-zone > h3 { margin: 0 0 5px; font-size: 0.86rem; font-weight: 600; color: var(--ink-2); }
.nm-zone.vpc { background: var(--cyan-soft); border-color: var(--cyan); }
.nm-zone.sub { background: var(--surface); border-style: solid; border-color: var(--rule); }
.nm-zone.sub > h3 { color: var(--ink-3); font-size: 0.78rem; margin-bottom: 4px; }
.nm-zone.home { background: var(--amber-soft); border-color: var(--amber); margin-top: 6px; }
.nm-arrow { text-align: center; color: var(--ink-3); font-size: 0.78rem; padding: 2px 0; line-height: 1.35; }
.nm-arrow b { color: var(--ink-2); font-weight: 600; }
.nm-arrow::before { content: "ARROW"; display: block; font-size: 1.05rem; color: var(--cyan); line-height: 1; }
.nm-side { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
.nm-side > * { flex: 1 1 140px; min-width: 0; }
.nm-key { margin: 8px 0 0; padding: 5px 8px; border-radius: 7px; background: var(--surface-2);
          font-size: 0.76rem; color: var(--ink-2); line-height: 1.45; }
.nm-key span { display: inline-block; width: 9px; height: 9px; border-radius: 3px; margin: 0 4px 0 1px; vertical-align: middle; }
""".replace("ARROW", ARROW)


def box(title, body, cls=""):
    return ('<div class="nm-box%s"><h4>%s</h4><p>%s</p></div>'
            % ((" " + cls) if cls else "", title, body))


def pick(s):
    return '<span class="pick">%s</span>' % s


HTML = "\n".join([
    '<div class="netmap">',
    '  <p class="lede">Where every networking question lives, top to bottom: the user, '
    'your VPC, the ways out.</p>',
    '  <div class="nm-row">',
    box("Route 53", "Which Region answers. %s: fastest. %s: by country. %s and a health "
        "check: a standby. %s: a share." % (pick("Latency"), pick("Geolocation"),
                                             pick("Failover"), pick("Weighted")), "edge"),
    box("CloudFront", "Caches near the user. %s, not many Regions. Only files? S3 behind it."
        % pick("One Region behind CloudFront"), "edge"),
    box("WAF and Shield", "Rules on web requests: CloudFront, ALB or API, %s. Big attack, "
        "team to call: Shield Advanced." % pick("never an NLB"), "edge"),
    '  </div>',
    '  <div class="nm-arrow"><b>Internet gateway</b>: one per VPC, in no zone</div>',
    '  <div class="nm-zone vpc">',
    '    <h3>Your VPC</h3>',
    '    <div class="nm-zone sub">',
    '      <h3>Public subnets, one per zone</h3>',
    '      <div class="nm-row">',
    box("Load balancer", "%s reads the request: paths, headers, logins, WAF. %s: fixed "
        "address or raw TCP." % (pick("ALB"), pick("NLB"))),
    box("NAT gateway", "Private subnets out, never in. %s in production; one shared for test."
        % pick("One per zone")),
    '      </div>',
    '    </div>',
    '    <div class="nm-arrow"><b>A route table per private subnet</b>, to its own zone\'s '
    'NAT gateway. A shared table sends every zone through one.</div>',
    '    <div class="nm-zone sub">',
    '      <h3>Private subnets, one per zone</h3>',
    '      <div class="nm-row">',
    box("Servers, containers, Lambda, database", "No public address. Lambda joins by being "
        "%s, not by VPN or endpoint. The database opens by security group to the servers "
        "only." % pick("attached to the VPC")),
    '      </div>',
    '    </div>',
    '    <div class="nm-side">',
    box("Gateway endpoint", "%s only. Free. Cuts the NAT bill." % pick("S3 and DynamoDB")),
    box("Interface endpoint, PrivateLink", "Any other AWS service, or %s, no internet. To "
        "offer yours: NLB with PrivateLink in front."
        % pick("another company's service on AWS")),
    '    </div>',
    '  </div>',
    '  <div class="nm-arrow">Out to other networks</div>',
    '  <div class="nm-row">',
    box("Transit gateway", "Hub for %s, accounts, sites. A route table each keeps VPCs "
        "apart. Two VPCs only: %s." % (pick("hundreds of VPCs"), pick("peering")), "hub"),
    '  </div>',
    '  <div class="nm-zone home">',
    '    <h3>Your own building</h3>',
    '    <div class="nm-row">',
    box("Direct Connect", "Private line. Steady, never the internet. Weeks to set up."),
    box("Site-to-Site VPN", "Encrypted over the internet. This week, costs little."),
    box("Both", "%s, when the link must not fail." % pick("Direct Connect, VPN as backup")),
    box("One line, many VPCs", "%s, usually into a transit gateway."
        % pick("Direct Connect gateway")),
    box("One person's laptop", "%s. Not for a whole building." % pick("Client VPN")),
    box("Names across the link", "%s: outbound asks your DNS, inbound lets it ask yours."
        % pick("Route 53 Resolver")),
    '    </div>',
    '  </div>',
    '  <div class="nm-key">',
    '    <span style="background: var(--cyan)"></span>the edge %s' % DOT,
    '    <span style="background: var(--magenta)"></span>joining networks %s' % DOT,
    '    <span style="background: var(--amber)"></span>your building.',
    '    Magenta text is the pick.',
    '  </div>',
    '</div>',
])

# ---- the standalone preview --------------------------------------------
PREVIEW = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Networking map</title>
<style>
:root {
  --surface: #fbfcfc; --surface-2: #e3ebed; --ink: #10181b; --ink-2: #46545a;
  --ink-3: #7b888d; --rule: #d3dde0; --cyan: #00707e; --cyan-soft: #d9eef1;
  --magenta: #99206c; --magenta-soft: #f7e3ef; --amber: #8a6508; --amber-soft: #fbf0d5;
}
body { margin: 0; padding: 16px; background: var(--surface); color: var(--ink);
       font: 15px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
.netmap .lede { color: var(--ink-2); line-height: 1.45; }
.netmap { max-width: 380px; margin: 0 auto; }
%s
</style>
</head>
<body>
%s
</body>
</html>
""" % (CSS, HTML)
if "--preview" in sys.argv:
    pathlib.Path(sys.argv[sys.argv.index("--preview") + 1]).write_bytes(PREVIEW.encode("utf-8"))

# ---- the poster ----------------------------------------------------------
raw = TEMPLATE.read_bytes().decode("utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
CSS_START, CSS_END = "/* NETMAP-CSS-START */", "/* NETMAP-CSS-END */"
HTML_START, HTML_END = "<!-- NETMAP-HTML-START -->", "<!-- NETMAP-HTML-END -->"


def put(text, start, end, block, anchor, before):
    """Replace what sits between the markers, or add it at the anchor."""
    if start in text:
        a, b = text.index(start), text.index(end) + len(end)
        return text[:a] + start + block + end + text[b:]
    if anchor not in text:
        raise SystemExit("could not find: " + anchor[:40])
    piece = start + block + end
    return text.replace(anchor, (piece + nl + nl + anchor) if before else (anchor + nl + nl + piece), 1)


css_block = nl + CSS.replace("\n", nl) + nl
raw = put(raw, CSS_START, CSS_END, css_block,
          ".dectraps li:last-child { margin-bottom: 0; }", before=False)

fold = nl.join([
    '    <details class="fold" id="fold-netmap" data-fold="netmap">',
    '      <summary>The networking map<span class="count">one picture</span></summary>',
    '      <div class="inner">',
    HTML.replace("\n", nl),
    '      </div>',
    '    </details>',
])
raw = put(raw, HTML_START, HTML_END, nl + fold + nl,
          '    <div class="board" id="board"></div>', before=True)

# The map is AWS networking. The other exams share the page but have nothing
# for it to show, so it is taken out of the page before the folds are read.
GATE = '    // NETMAP-GATE' + nl + \
       '    if (EXAM !== "saa-c03") {' + nl + \
       '      var nm = document.getElementById("fold-netmap");' + nl + \
       '      if (nm) nm.parentNode.removeChild(nm);' + nl + \
       '    }' + nl
if "// NETMAP-GATE" not in raw:
    anchor = '  (function rememberFolds() {' + nl
    if anchor not in raw:
        raise SystemExit("could not find rememberFolds")
    raw = raw.replace(anchor, anchor + GATE, 1)

for ch in raw:
    if ord(ch) < 32 and ch not in "\r\n":
        raise SystemExit("a control character crept in")
TEMPLATE.write_bytes(raw.encode("utf-8"))
print("map written: preview and poster")
