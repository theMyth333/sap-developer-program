#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds a 45-minute marketing webinar deck:
"Build Enterprise Apps with SAP BTP + CAPM + AI"
Audience: freshers / recent graduates / aspiring developers.
Facts are conservative and sourced; illustrative items are labelled.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ----------------------------------------------------------------------------
# Palette (SAP Horizon-inspired, restrained)
# ----------------------------------------------------------------------------
NAVY      = RGBColor(0x0A, 0x25, 0x40)   # dark navy
NAVY2     = RGBColor(0x10, 0x33, 0x55)
BLUE      = RGBColor(0x00, 0x70, 0xF2)   # SAP Horizon blue
BLUE_LT   = RGBColor(0xD6, 0xE4, 0xFF)
BLUE_XLT  = RGBColor(0xED, 0xF4, 0xFF)
TEAL      = RGBColor(0x0A, 0x9A, 0x8C)
AMBER     = RGBColor(0xF0, 0xA0, 0x18)   # used for AI accents
RED       = RGBColor(0xD4, 0x3A, 0x3A)
GREEN     = RGBColor(0x1C, 0x8E, 0x4A)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
GRAY_BG   = RGBColor(0xF4, 0xF6, 0xFA)
GRAY_MID  = RGBColor(0xC9, 0xD2, 0xDE)
GRAY_TX   = RGBColor(0x5A, 0x67, 0x78)
INK       = RGBColor(0x1B, 0x2A, 0x3A)

FONT   = "Segoe UI"
FONTSB = "Segoe UI Semibold"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def slide():
    return prs.slides.add_slide(BLANK)

def bg(s, color):
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = color

def _set_font(run, size, color, bold, font, italic=False):
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font

def tb(s, l, t, w, h, lines, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT,
       font=FONT, anchor=MSO_ANCHOR.TOP, space_after=4, line_spacing=1.0, wrap=True):
    """lines: str OR list of (text,size,color,bold[,italic]) tuples OR list of str."""
    box = s.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0
    tf.margin_top = 0; tf.margin_bottom = 0
    if isinstance(lines, str):
        lines = [lines]
    first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.space_after = Pt(space_after)
        p.space_before = Pt(0)
        p.line_spacing = line_spacing
        if isinstance(ln, tuple):
            text = ln[0]; sz = ln[1] if len(ln) > 1 else size
            col = ln[2] if len(ln) > 2 else color
            bd  = ln[3] if len(ln) > 3 else bold
            it  = ln[4] if len(ln) > 4 else False
            fnt = ln[5] if len(ln) > 5 else font
            r = p.add_run(); r.text = text; _set_font(r, sz, col, bd, fnt, it)
        else:
            r = p.add_run(); r.text = str(ln); _set_font(r, size, color, bold, font)
    return box

def rect(s, l, t, w, h, fill=None, line=None, line_w=1.0, rounded=False, shadow=False):
    shp = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE, l, t, w, h)
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line; shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    if rounded:
        try:
            shp.adjustments[0] = 0.08
        except Exception:
            pass
    return shp

def shp_text(shp, lines, size=14, color=INK, bold=False, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE, font=FONT, space_after=2, line_spacing=1.0):
    tf = shp.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = Pt(6); tf.margin_right = Pt(6)
    tf.margin_top = Pt(4); tf.margin_bottom = Pt(4)
    if isinstance(lines, str):
        lines = [lines]
    first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align; p.space_after = Pt(space_after); p.space_before = Pt(0)
        p.line_spacing = line_spacing
        if isinstance(ln, tuple):
            r = p.add_run(); r.text = ln[0]
            _set_font(r, ln[1] if len(ln)>1 else size, ln[2] if len(ln)>2 else color,
                      ln[3] if len(ln)>3 else bold, ln[5] if len(ln)>5 else font,
                      ln[4] if len(ln)>4 else False)
        else:
            r = p.add_run(); r.text = str(ln); _set_font(r, size, color, bold, font)

def arrow(s, l, t, w, h, fill=BLUE, direction="right"):
    shape = {"right": MSO_SHAPE.RIGHT_ARROW, "down": MSO_SHAPE.DOWN_ARROW,
             "chev": MSO_SHAPE.CHEVRON}.get(direction, MSO_SHAPE.RIGHT_ARROW)
    a = s.shapes.add_shape(shape, l, t, w, h)
    a.fill.solid(); a.fill.fore_color.rgb = fill
    a.line.fill.background(); a.shadow.inherit = False
    return a

def line_connector(s, x1, y1, x2, y2, color=GRAY_MID, w=1.5, dash=False):
    c = s.shapes.add_connector(2, x1, y1, x2, y2)
    c.line.color.rgb = color; c.line.width = Pt(w); c.shadow.inherit = False
    if dash:
        ln = c.line._get_or_add_ln()
        d = ln.makeelement(qn('a:prstDash'), {'val': 'dash'}); ln.append(d)
    return c

def notes(s, text):
    s.notes_slide.notes_text_frame.text = text.strip()

# content-slide chrome: kicker band + title + footer
def header(s, kicker, title, minutes=None):
    bg(s, WHITE)
    rect(s, 0, 0, SW, Inches(1.18), fill=NAVY)
    rect(s, 0, Inches(1.18), SW, Pt(3), fill=BLUE)
    tb(s, Inches(0.55), Inches(0.17), Inches(9.5), Inches(0.3),
       [(kicker.upper(), 12, BLUE_LT, True)], font=FONTSB)
    tb(s, Inches(0.55), Inches(0.44), Inches(10.6), Inches(0.66),
       [(title, 25, WHITE, True)], font=FONTSB, anchor=MSO_ANCHOR.MIDDLE)
    if minutes:
        chip = rect(s, Inches(11.55), Inches(0.33), Inches(1.25), Inches(0.52),
                    fill=BLUE, rounded=True)
        shp_text(chip, [(minutes, 13, WHITE, True)])
    # footer
    tb(s, Inches(0.55), Inches(7.12), Inches(8), Inches(0.3),
       [("SAP BTP + CAPM + AI  |  Developer Training Webinar", 9, GRAY_TX, False)])
    tb(s, Inches(11.6), Inches(7.12), Inches(1.2), Inches(0.3),
       [(str(len(prs.slides._sldIdLst)) if False else "", 9, GRAY_TX, False)], align=PP_ALIGN.RIGHT)

def pagenum(s, n):
    tb(s, Inches(12.3), Inches(7.12), Inches(0.6), Inches(0.3),
       [(str(n), 9, GRAY_TX, True)], align=PP_ALIGN.RIGHT)

def chip(s, l, t, w, text, fill=BLUE_XLT, txt=BLUE, h=Inches(0.42), size=12, bold=True):
    c = rect(s, l, t, w, h, fill=fill, rounded=True)
    shp_text(c, [(text, size, txt, bold)])
    return c

# ============================================================================
# SLIDE 1 — TITLE
# ============================================================================
s = slide(); bg(s, NAVY)
rect(s, 0, 0, SW, SH, fill=NAVY)
# accent band
rect(s, 0, Inches(5.95), SW, Inches(0.08), fill=BLUE)
rect(s, 0, 0, Inches(0.18), SH, fill=BLUE)
# decorative blocks top-right
for i, (dx, col) in enumerate([(0, BLUE), (0.55, TEAL), (1.1, AMBER)]):
    rect(s, Inches(11.1 + dx), Inches(0.6), Inches(0.42), Inches(0.42),
         fill=col, rounded=True)
tb(s, Inches(0.9), Inches(1.5), Inches(11), Inches(0.5),
   [("DEVELOPER TRAINING WEBINAR", 15, BLUE_LT, True)], font=FONTSB)
tb(s, Inches(0.9), Inches(2.05), Inches(11.6), Inches(2.0),
   [("Build Enterprise Apps with", 40, WHITE, True),
    ("SAP BTP, CAPM & AI", 52, WHITE, True)], font=FONTSB, line_spacing=1.02)
tb(s, Inches(0.9), Inches(4.35), Inches(11), Inches(0.6),
   [("From zero SAP knowledge to a deployed, cloud-native business application", 18, BLUE_LT, False)])
tb(s, Inches(0.9), Inches(6.2), Inches(11.5), Inches(0.9),
   [("A career-focused program for freshers, graduates and aspiring developers", 14, GRAY_MID, False),
    ("45-minute session  •  Live demo included  •  Q&A", 13, WHITE, True)], space_after=4)
notes(s, """
KEY MESSAGE: Welcome people and set an inspiring, credible tone. This is a doorway from "I can code a little" to "I can build and deploy real enterprise software."

SCRIPT: "Welcome, everyone. Over the next 45 minutes I'll show you how modern enterprise software is built, why SAP sits at the centre of it, and how a beginner can realistically learn to build and deploy a real cloud application on SAP's platform - with AI helping you every step of the way. No prior SAP knowledge is needed; if you can write a little code and you're curious, you're in the right room."

ENGAGEMENT: Quick poll in chat - "Type 1 if you've heard of SAP, 2 if it's brand new to you." This tells you how much grounding the room needs.

DELIVERY TIME: ~30 seconds. Keep energy high; don't read the slide.

TRANSITION: "Let me start with why any of this matters - with software you already use without realising it."
""")

# ============================================================================
# SLIDE 2 — AGENDA (45-min, corrected)
# ============================================================================
s = slide(); header(s, "What we'll cover", "Your 45 Minutes, Mapped")
rows = [
    ("1", "Why businesses need connected software (the problem)", "2 min", TEAL),
    ("2", "ERP & SAP fundamentals", "4 min", TEAL),
    ("3", "Cloud evolution & SAP BTP", "5 min", BLUE),
    ("4", "SAP CAPM: how modern apps are built", "6 min", BLUE),
    ("5", "How AI is changing the development lifecycle", "4 min", AMBER),
    ("6", "Career paths & industry relevance", "2 min", TEAL),
    ("7", "Training curriculum walkthrough", "2 min", TEAL),
    ("8", "Live demo: build a CAP service", "10 min", BLUE),
    ("9", "Q&A + next steps", "10 min", NAVY),
]
y = Inches(1.5)
rh = Inches(0.55)
for i, (n, label, mins, col) in enumerate(rows):
    yy = y + rh * i
    band = GRAY_BG if i % 2 == 0 else WHITE
    rect(s, Inches(0.55), yy, Inches(12.2), rh - Pt(4), fill=band)
    num = rect(s, Inches(0.7), yy + Pt(4), Inches(0.5), Inches(0.42), fill=col, rounded=True)
    shp_text(num, [(n, 14, WHITE, True)])
    tb(s, Inches(1.45), yy, Inches(8.8), rh, [(label, 15, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE)
    tb(s, Inches(10.9), yy, Inches(1.7), rh, [(mins, 14, col, True)],
       anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
tb(s, Inches(0.55), Inches(6.65), Inches(12), Inches(0.3),
   [("25 min teaching  +  10 min live demo  +  10 min Q&A  =  45 minutes", 13, GRAY_TX, True)],
   align=PP_ALIGN.CENTER)
pagenum(s, 2)
notes(s, """
KEY MESSAGE: Set expectations and show that the demo and Q&A are protected time.

SCRIPT: "Here's how we'll spend our time. About 25 minutes of teaching that takes you from the business problem all the way to how real apps are built, then a 10-minute live demo where I build something in front of you, and 10 minutes for your questions. I'll keep an eye on the clock so the demo and your questions aren't squeezed."

NOTE ON TIMING: The original planning agenda accidentally summed to 55 minutes. This corrected agenda is exactly 45: teaching 2+4+5+6+4+2+2 = 25, demo 10, Q&A 10.

DELIVERY TIME: ~30 seconds.

TRANSITION: "Let's start with a company that looks a lot like businesses you already buy from."
""")

# ============================================================================
# SLIDE 3 — HOOK + DISCONNECTED SYSTEMS SCENARIO
# ============================================================================
s = slide(); header(s, "The problem", "Great Products, Disconnected Systems", "2 min")
tb(s, Inches(0.55), Inches(1.35), Inches(12), Inches(0.5),
   [("Meet ", 17, INK, False), ("\"NorthWind Retail\"", 17, BLUE, True),
    (" - a growing company selling online and in stores. (Illustrative example)", 15, GRAY_TX, False)])
silos = [
    ("Sales", "Orders in\na spreadsheet"),
    ("Inventory", "Stock counts\nin a 2nd system"),
    ("Finance", "Invoices in\naccounting tool"),
    ("Procurement", "Emails &\nPDFs to suppliers"),
    ("Reporting", "Manual\nmonth-end merge"),
]
bx = Inches(0.55); bw = Inches(2.104); gap = Inches(0.42); by = Inches(2.35); bh = Inches(1.55)
for i, (t, d) in enumerate(silos):
    x = bx + (bw + gap) * i
    rect(s, x, by, bw, bh, fill=WHITE, line=GRAY_MID, line_w=1.25, rounded=True)
    rect(s, x, by, bw, Inches(0.1), fill=GRAY_TX)
    tb(s, x, by + Inches(0.28), bw, Inches(0.4), [(t, 15, NAVY, True)], align=PP_ALIGN.CENTER)
    tb(s, x + Inches(0.1), by + Inches(0.74), bw - Inches(0.2), Inches(0.72),
       [(d, 12, GRAY_TX, False)], align=PP_ALIGN.CENTER, line_spacing=1.05)
    # "disconnected" badge, centred in the gap so it never overlaps a card
    if i < len(silos) - 1:
        mw = Inches(0.36)
        mx = x + bw + (gap - mw) / 2
        my = by + bh / 2 - mw / 2
        badge = rect(s, mx, my, mw, mw, fill=RED, rounded=True)
        shp_text(badge, [("≠", 15, WHITE, True)])
tb(s, Inches(0.55), Inches(3.96), Inches(12.2), Inches(0.3),
   [("≠  each tool holds its own data and cannot share it", 12, RED, True)],
   align=PP_ALIGN.CENTER)
# consequences
rect(s, Inches(0.55), Inches(4.35), Inches(12.2), Inches(2.1), fill=BLUE_XLT, rounded=True)
tb(s, Inches(0.85), Inches(4.5), Inches(11.6), Inches(0.4),
   [("What goes wrong when systems don't talk to each other:", 15, NAVY, True)])
cons = [
    "The same data is typed in 3 times - and three versions disagree",
    "Sold stock that wasn't really there; late orders and unhappy customers",
    "Finance waits days to know what was actually sold",
    "Leaders make decisions on numbers that are already out of date",
]
for i, c in enumerate(cons):
    col = i % 2; row = i // 2
    x = Inches(0.95) + Inches(6.0) * col
    yy = Inches(4.98) + Inches(0.68) * row
    dot = rect(s, x, yy + Inches(0.06), Inches(0.14), Inches(0.14), fill=RED, rounded=True)
    tb(s, x + Inches(0.3), yy, Inches(5.4), Inches(0.62), [(c, 13, INK, False)], line_spacing=1.0)
pagenum(s, 3)
notes(s, """
KEY MESSAGE: Fragmented systems create duplicated data, errors, and slow decisions. Everyone has felt this pain, even outside SAP.

SCRIPT: "Imagine a retailer, NorthWind - this is an illustrative example, not a real customer. Sales live in a spreadsheet. Inventory is a different tool. Finance is a third. Procurement is email and PDFs. Each one works fine on its own. The trouble is the gaps between them. The same order gets typed in three times, and now you have three 'truths'. You sell something that was already out of stock. Finance finds out what sold days later. And the boss is making decisions on last week's numbers."

ANALOGY: "It's like five brilliant people in five rooms with the doors shut, passing notes under the door. Each is smart; together they're slow and error-prone."

ENGAGEMENT: "Drop a 'yes' in chat if you've seen a spreadsheet run a whole department." Most will say yes.

DELIVERY TIME: ~1 minute.

TRANSITION: "There's a name for the system that knocks down those walls - ERP."
""")

# ============================================================================
# SLIDE 4 — WHAT IS ERP
# ============================================================================
s = slide(); header(s, "ERP & SAP fundamentals", "ERP: One Shared Source of Truth", "4 min")
tb(s, Inches(0.55), Inches(1.35), Inches(12.2), Inches(0.55),
   [("Enterprise Resource Planning", 17, BLUE, True),
    (" - software that connects a company's core functions around one shared set of data.", 16, INK, False)])
# central hub + spokes
cx, cy = Inches(6.55), Inches(4.25)
hub = rect(s, cx - Inches(1.15), cy - Inches(0.75), Inches(2.3), Inches(1.5),
           fill=NAVY, rounded=True)
shp_text(hub, [("ERP", 22, WHITE, True), ("one shared", 11, BLUE_LT, False),
               ("database", 11, BLUE_LT, False)])
spokes = [
    ("Sales", Inches(2.0), Inches(2.25)),
    ("Finance", Inches(9.3), Inches(2.25)),
    ("Inventory", Inches(1.1), Inches(4.05)),
    ("Procurement", Inches(10.2), Inches(4.05)),
    ("HR", Inches(2.0), Inches(5.85)),
    ("Reporting", Inches(9.3), Inches(5.85)),
]
for t, x, y in spokes:
    node = rect(s, x, y, Inches(2.0), Inches(0.72), fill=BLUE_XLT, line=BLUE, line_w=1.25, rounded=True)
    shp_text(node, [(t, 14, NAVY, True)])
    line_connector(s, int(x + Inches(1.0)), int(y + Inches(0.36)),
                   int(cx), int(cy), color=GRAY_MID, w=1.5)
tb(s, Inches(0.55), Inches(6.7), Inches(12.2), Inches(0.4),
   [("Enter data once  →  every function sees the same, up-to-date reality in real time.",
     14, TEAL, True)], align=PP_ALIGN.CENTER)
pagenum(s, 4)
notes(s, """
KEY MESSAGE: ERP = one integrated system and one shared database across core business functions, so data is entered once and trusted everywhere.

SCRIPT: "ERP stands for Enterprise Resource Planning. Forget the jargon - the idea is simple. Instead of each department keeping its own copy of the data, ERP puts the core functions around one shared database. Sell an item, and inventory, finance, and reporting all update from the same record, instantly. Enter data once; everyone sees the same truth."

ANALOGY: "Open the five doors and put everyone around one table looking at one screen. That's ERP."

WHY ORGANISATIONS USE IT: fewer errors, real-time visibility, standard processes, auditability, and the ability to scale without adding chaos.

DELIVERY TIME: ~1 minute.

SOURCE: 'Enterprise Resource Planning' is a standard industry term; SAP and other vendors define ERP as integrated management of core business processes via a shared database.

TRANSITION: "To make the payoff concrete, here's the same company before and after ERP."
""")

# ============================================================================
# SLIDE 5 — BEFORE vs AFTER
# ============================================================================
s = slide(); header(s, "ERP & SAP fundamentals", "Before vs After Integration")
# two panels
pw = Inches(6.0); ph = Inches(4.9); py = Inches(1.55)
# BEFORE
rect(s, Inches(0.55), py, pw, Inches(0.6), fill=RED, rounded=False)
tb(s, Inches(0.55), py, pw, Inches(0.6), [("BEFORE  -  disconnected tools", 16, WHITE, True)],
   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, Inches(0.55), py + Inches(0.6), pw, ph - Inches(0.6), fill=GRAY_BG, line=GRAY_MID, line_w=1)
before = [
    "Data re-keyed into many systems",
    "Conflicting numbers, no single truth",
    "Manual, slow month-end reporting",
    "Stock-outs and overselling",
    "Hard to audit; errors hide in silos",
    "Growth multiplies the chaos",
]
for i, t in enumerate(before):
    yy = py + Inches(0.95) + Inches(0.63) * i
    tb(s, Inches(0.85), yy, Inches(0.4), Inches(0.5), [("✕", 15, RED, True)])
    tb(s, Inches(1.25), yy, Inches(5.1), Inches(0.55), [(t, 13.5, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE)
# AFTER
ax = Inches(6.78)
rect(s, ax, py, pw, Inches(0.6), fill=GREEN)
tb(s, ax, py, pw, Inches(0.6), [("AFTER  -  integrated ERP", 16, WHITE, True)],
   align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rect(s, ax, py + Inches(0.6), pw, ph - Inches(0.6), fill=BLUE_XLT, line=BLUE, line_w=1)
after = [
    "Enter once, shared everywhere",
    "One trusted source of truth",
    "Real-time dashboards and reports",
    "Accurate, visible stock levels",
    "Traceable, audit-ready processes",
    "Standard processes that scale",
]
for i, t in enumerate(after):
    yy = py + Inches(0.95) + Inches(0.63) * i
    tb(s, ax + Inches(0.3), yy, Inches(0.4), Inches(0.5), [("✓", 15, GREEN, True)])
    tb(s, ax + Inches(0.7), yy, Inches(5.1), Inches(0.55), [(t, 13.5, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE)
pagenum(s, 5)
notes(s, """
KEY MESSAGE: Integration turns scattered effort into a reliable, scalable operation - this is why companies invest heavily in ERP.

SCRIPT: "Same company, two worlds. On the left, before: re-keyed data, arguments about whose number is right, month-end that eats a week, stock-outs. On the right, after: enter once and it's shared, one trusted source of truth, real-time reporting, audit-ready. The important part for your career: the 'after' column is work. Someone has to model that data, build those services, secure them, and deploy them. That 'someone' is the developer we're training you to become."

DELIVERY TIME: ~1 minute. Let the contrast land; don't read every row.

TRANSITION: "The best-known company for building this kind of software is SAP."
""")

# ============================================================================
# SLIDE 6 — WHAT IS SAP
# ============================================================================
s = slide(); header(s, "ERP & SAP fundamentals", "What Is SAP - and Why It Matters")
tb(s, Inches(0.55), Inches(1.35), Inches(7.1), Inches(1.1),
   [("SAP is a German software company (founded 1972, HQ Walldorf) and the world's largest vendor of enterprise software.",
     16, INK, False)],
   line_spacing=1.08)
tb(s, Inches(0.55), Inches(2.55), Inches(7.1), Inches(0.5),
   [("Its modern ERP is ", 16, INK, False), ("SAP S/4HANA", 16, BLUE, True),
    (", run in the cloud or on-premise.", 16, INK, False)])
# fact cards
facts = [
    ("1972", "Founded; HQ in\nWalldorf, Germany"),
    ("#1", "World's largest\nenterprise software vendor"),
    ("98 of 100", "of the world's largest\ncompanies are SAP customers*"),
    ("~110,000", "employees\nworldwide (2025)"),
]
fx = Inches(0.55); fw = Inches(1.72); fgap = Inches(0.1); fy = Inches(3.35)
for i, (big, sub) in enumerate(facts):
    x = fx + (fw + fgap) * i
    rect(s, x, fy, fw, Inches(1.45), fill=NAVY, rounded=True)
    tb(s, x, fy + Inches(0.18), fw, Inches(0.5), [(big, 21, WHITE, True)], align=PP_ALIGN.CENTER)
    tb(s, x, fy + Inches(0.72), fw, Inches(0.7), [(sub, 10.5, BLUE_LT, False)],
       align=PP_ALIGN.CENTER, line_spacing=1.0)
# industries panel
rect(s, Inches(7.95), Inches(1.35), Inches(4.8), Inches(3.55), fill=GRAY_BG, line=GRAY_MID, line_w=1, rounded=True)
tb(s, Inches(8.2), Inches(1.5), Inches(4.3), Inches(0.4), [("Used across industries", 15, NAVY, True)])
inds = ["Manufacturing", "Retail", "Finance & Banking", "Logistics & Supply Chain",
        "Healthcare", "Energy & Utilities", "Public Sector"]
for i, t in enumerate(inds):
    yy = Inches(2.0) + Inches(0.4) * i
    dot = rect(s, Inches(8.25), yy + Inches(0.07), Inches(0.12), Inches(0.12), fill=BLUE, rounded=True)
    tb(s, Inches(8.5), yy, Inches(4.1), Inches(0.36), [(t, 13, INK, False)], anchor=MSO_ANCHOR.MIDDLE)
tb(s, Inches(0.55), Inches(5.05), Inches(12.2), Inches(1.6),
   [("Why it matters for you: ", 14, TEAL, True),
    ("huge global install base means long-lived systems, steady demand for people who can build and extend them, and skills that transfer across industries and countries.",
     14, INK, False)], line_spacing=1.1)
tb(s, Inches(0.55), Inches(6.78), Inches(12), Inches(0.3),
   [("* \"98 of the 100 largest companies are SAP customers\" and \"world's largest enterprise software vendor\" are SAP / widely-reported figures - verify current wording before quoting on stage.",
     9.5, GRAY_TX, False, True)])
pagenum(s, 6)
notes(s, """
KEY MESSAGE: SAP is the dominant enterprise-software vendor; its scale is exactly why SAP skills are durable and in demand.

SCRIPT: "SAP is a German company, founded in 1972, headquartered in Walldorf, and it's the world's largest vendor of enterprise software. Its modern ERP is called SAP S/4HANA. A widely-quoted figure is that 98 of the 100 largest companies in the world are SAP customers, and SAP employs around 110,000 people. You'll find SAP in manufacturing, retail, banking, logistics, healthcare and the public sector."

HONESTY GUARDRAIL: Present '98 of 100' and '#1 vendor' as SAP / widely-reported claims, not your own measurement. Avoid unverified 'X% of global transactions' statistics. The footnote on the slide says to verify wording before quoting.

SOURCES: SAP company facts (founded 1972, Walldorf, world's largest enterprise software vendor, ~110,000 employees as of 2025) per SAP corporate materials and encyclopaedic summaries; '98 of 100 largest companies' is a commonly cited SAP figure.

WHY INVEST: companies spend on SAP because it standardises and de-risks core operations; that long life means steady work for developers.

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "For decades, building on SAP meant one main language and one main place - the core system. That has changed. Here's how."
""")

# ============================================================================
# SLIDE 7 — EVOLUTION TIMELINE
# ============================================================================
s = slide(); header(s, "Cloud evolution & SAP BTP", "How SAP Development Evolved", "5 min")
stages = [
    ("Classic ERP", "On-premise SAP.\nCustom logic written in\nABAP, inside the core.", NAVY),
    ("Customisation\nin the core", "Powerful, but changes\nmake upgrades slow\nand risky.", NAVY2),
    ("Cloud & APIs", "IaaS/PaaS/SaaS.\nApps talk over APIs;\nloosely-coupled services.", BLUE),
    ("Keep the core clean", "Build extensions\nalongside the core, not\ninside it (\"clean core\").", TEAL),
    ("Cloud-native\ndevelopment", "Build with JS/Node.js\non SAP BTP using CAP -\nupgrade-safe.", GREEN),
]
n = len(stages); tw = Inches(2.3); gap = Inches(0.17)
tx0 = Inches(0.55); ty = Inches(2.1); th = Inches(2.35)
# baseline
line_connector(s, int(Inches(0.7)), int(Inches(1.85)), int(Inches(12.7)), int(Inches(1.85)),
               color=GRAY_MID, w=2)
for i, (title, body, col) in enumerate(stages):
    x = tx0 + (tw + gap) * i
    dot = rect(s, x + tw/2 - Inches(0.1), Inches(1.75), Inches(0.2), Inches(0.2), fill=col, rounded=True)
    card = rect(s, x, ty, tw, th, fill=WHITE, line=col, line_w=1.5, rounded=True)
    rect(s, x, ty, tw, Inches(0.12), fill=col)
    tb(s, x, ty + Inches(0.22), tw, Inches(0.72), [(title, 14, col, True)],
       align=PP_ALIGN.CENTER, line_spacing=0.95)
    tb(s, x + Inches(0.12), ty + Inches(1.0), tw - Inches(0.24), Inches(1.25),
       [(body, 11.5, INK, False)], align=PP_ALIGN.CENTER, line_spacing=1.03)
    if i < n - 1:
        arrow(s, x + tw + Inches(0.01), ty + Inches(1.0), Inches(0.15), Inches(0.3), fill=col)
tb(s, Inches(0.55), Inches(4.75), Inches(12.2), Inches(1.6),
   [("The big idea - \"Clean Core\": ", 15, TEAL, True),
    ("keep the standard SAP system standard so it stays easy to upgrade, and put your custom apps and logic beside it on SAP BTP. That side-by-side space is where modern SAP developers - and this course - live.",
     15, INK, False)], line_spacing=1.12)
tb(s, Inches(0.55), Inches(6.35), Inches(12.2), Inches(0.5),
   [("Conceptual timeline - ABAP still matters; CAPM is the modern, cloud-native path that complements it.",
     12, GRAY_TX, False, True)])
pagenum(s, 7)
notes(s, """
KEY MESSAGE: SAP development moved from writing ABAP inside the core to building upgrade-safe, cloud-native extensions beside the core on SAP BTP. "Clean core" is the governing principle.

SCRIPT: "For decades, SAP development meant ABAP - SAP's own programming language - and you wrote your customisations right inside the core system. It was powerful, but every change made upgrades harder and riskier. Then the whole industry moved to the cloud and to APIs: small services that talk to each other instead of one giant block of code. SAP embraced this with an idea called 'clean core' - keep the standard system standard so it upgrades smoothly, and build your custom apps beside it. That 'beside it' place is SAP BTP, and the modern way to build there is CAP."

CLARIFY (don't overclaim): ABAP is not dead - it's still widely used and valuable. CAPM is the modern cloud-native path that complements ABAP/UI5/Fiori skills; it doesn't replace them.

ANALOGY: "Don't remodel the load-bearing walls of the house every time you want a new room. Build an extension."

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "So what exactly is this platform beside the core? That's SAP BTP."
""")

# ============================================================================
# SLIDE 8 — WHAT IS SAP BTP
# ============================================================================
s = slide(); header(s, "Cloud evolution & SAP BTP", "SAP BTP: The Platform to Build On")
tb(s, Inches(0.55), Inches(1.32), Inches(12.2), Inches(0.9),
   [("SAP ", 16, INK, False), ("Business Technology Platform", 16, BLUE, True),
    (" is SAP's cloud platform for building, integrating, automating and adding AI to applications - all in one place, next to your SAP systems.",
     16, INK, False)], line_spacing=1.1)
caps = [
    ("App Development\n& Automation", "Build apps (CAP, Fiori)\nand automate processes\n(SAP Build)", BLUE),
    ("Integration", "Connect SAP and\nnon-SAP systems and\nAPIs reliably", TEAL),
    ("Data & Analytics", "SAP HANA Cloud,\ndatabases and\nbusiness insight", NAVY),
    ("Artificial\nIntelligence", "SAP AI Core &\nGenerative AI Hub to\nadd AI to apps", AMBER),
]
cw = Inches(2.95); cgap = Inches(0.17); cx0 = Inches(0.55); cy = Inches(2.55); ch = Inches(2.1)
for i, (t, d, col) in enumerate(caps):
    x = cx0 + (cw + cgap) * i
    rect(s, x, cy, cw, ch, fill=WHITE, line=col, line_w=1.5, rounded=True)
    rect(s, x, cy, cw, Inches(0.5), fill=col)
    shp_text(rect(s, x, cy, cw, Inches(0.5), fill=col), [(t, 13.5, WHITE, True)])
    tb(s, x + Inches(0.15), cy + Inches(0.65), cw - Inches(0.3), Inches(1.3),
       [(d, 12.5, INK, False)], align=PP_ALIGN.CENTER, line_spacing=1.08)
rect(s, Inches(0.55), Inches(4.95), Inches(12.2), Inches(1.45), fill=BLUE_XLT, rounded=True)
tb(s, Inches(0.85), Inches(5.12), Inches(11.6), Inches(1.2),
   [("Example (illustrative): ", 14, NAVY, True),
    ("a company builds a \"Supplier Onboarding\" app on BTP. It stores its own data, reads vendor master data from S/4HANA through an API, adds approval logic, and shows a clean Fiori screen - without touching the core system.",
     14, INK, False)], line_spacing=1.12)
tb(s, Inches(0.55), Inches(6.5), Inches(12.2), Inches(0.4),
   [("Remember: BTP is the platform (the \"where\"). CAPM is a development model used to build apps on it (the \"how\").",
     13, TEAL, True)], align=PP_ALIGN.CENTER)
pagenum(s, 8)
notes(s, """
KEY MESSAGE: SAP BTP is the single cloud platform where you build, integrate, analyse data, and add AI - beside SAP's core systems. Keep the platform-vs-model distinction crisp.

SCRIPT: "SAP BTP - Business Technology Platform - is SAP's cloud platform for building things next to your SAP systems. Think of four big capability areas: building and automating apps, integrating systems, data and analytics with SAP HANA Cloud, and AI services. The business problem it solves: you can extend and modernise SAP without risky changes to the core, and you can connect SAP and non-SAP systems in one governed place."

ILLUSTRATIVE EXAMPLE: supplier onboarding app - label it as illustrative, not a named customer.

CRITICAL DISTINCTION (repeat it): "BTP is the WHERE. CAPM is the HOW. Platform versus programming model." You'll reinforce this on the next slides.

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "Let me show how an app on BTP actually fits with the core system - then we'll open up CAP itself."
""")

# ============================================================================
# SLIDE 9 — BTP ARCHITECTURE DIAGRAM
# ============================================================================
s = slide(); header(s, "Cloud evolution & SAP BTP", "Side-by-Side: How It Fits Together")
# Users (left)
def diagram_box(x, y, w, h, title, sub, fill, tcol=WHITE, scol=None, line=None):
    r = rect(s, x, y, w, h, fill=fill, line=line, line_w=1.5, rounded=True)
    shp_text(r, [(title, 15, tcol, True)] + ([(sub, 11, scol or tcol, False)] if sub else []),
             line_spacing=1.0)
    return r
uy = Inches(3.1)
diagram_box(Inches(0.55), uy, Inches(2.0), Inches(1.3), "Users", "Browser / mobile\n(Fiori apps)", BLUE)
# BTP container
rect(s, Inches(3.15), Inches(1.7), Inches(6.5), Inches(4.5), fill=BLUE_XLT, line=BLUE, line_w=1.75, rounded=True)
tb(s, Inches(3.35), Inches(1.82), Inches(6.1), Inches(0.4), [("SAP BTP  (cloud platform)", 15, NAVY, True)])
# CAP app inside
rect(s, Inches(3.5), Inches(2.35), Inches(5.8), Inches(2.55), fill=WHITE, line=TEAL, line_w=1.75, rounded=True)
tb(s, Inches(3.65), Inches(2.45), Inches(5.5), Inches(0.35), [("Your app, built with CAPM", 14, TEAL, True)])
inner = [
    ("Fiori UI", BLUE),
    ("OData / REST API", NAVY),
    ("Business logic (Node.js)", TEAL),
    ("Data model (CDS)", NAVY2),
]
for i, (t, c) in enumerate(inner):
    yy = Inches(2.85) + Inches(0.48) * i
    r = rect(s, Inches(3.75), yy, Inches(5.3), Inches(0.4), fill=GRAY_BG, line=c, line_w=1, rounded=True)
    shp_text(r, [(t, 12.5, INK, True)])
# HANA Cloud inside BTP
r = rect(s, Inches(3.5), Inches(5.05), Inches(5.8), Inches(0.95), fill=NAVY, rounded=True)
shp_text(r, [("SAP HANA Cloud", 14, WHITE, True), ("the app's cloud database", 10.5, BLUE_LT, False)])
# S/4HANA (right)
diagram_box(Inches(10.25), Inches(2.35), Inches(2.55), Inches(1.6), "SAP S/4HANA",
            "the core ERP\n(kept clean)", NAVY)
# External (right lower)
diagram_box(Inches(10.25), Inches(4.3), Inches(2.55), Inches(1.5), "External systems",
            "other APIs,\npartners, services", TEAL)
# arrows
arrow(s, Inches(2.6), uy + Inches(0.5), Inches(0.5), Inches(0.3), fill=BLUE)
line_connector(s, int(Inches(9.3)), int(Inches(3.6)), int(Inches(10.25)), int(Inches(3.15)), color=BLUE, w=2.5)
line_connector(s, int(Inches(9.3)), int(Inches(4.2)), int(Inches(10.25)), int(Inches(5.05)), color=TEAL, w=2.5)
tb(s, Inches(9.25), Inches(2.95), Inches(1.1), Inches(0.3), [("API", 11, BLUE, True)], align=PP_ALIGN.CENTER)
tb(s, Inches(9.25), Inches(4.5), Inches(1.1), Inches(0.3), [("API", 11, TEAL, True)], align=PP_ALIGN.CENTER)
tb(s, Inches(0.55), Inches(6.55), Inches(12.2), Inches(0.5),
   [("Your CAPM app lives on BTP with its own data, and reaches into S/4HANA and other systems through APIs - the core stays clean.",
     13, GRAY_TX, True)], align=PP_ALIGN.CENTER)
pagenum(s, 9)
notes(s, """
KEY MESSAGE: Concrete mental model - users hit a Fiori UI; the CAP app on BTP has its own data model, logic, API and HANA Cloud database; it talks to S/4HANA and external systems through APIs. The core is never modified.

SCRIPT: "Follow the picture left to right. Users open a Fiori app in a browser. That app runs on SAP BTP and is built with CAP: a data model, business logic in Node.js, an API, and a user interface, backed by its own SAP HANA Cloud database. When it needs real company data - say a vendor or a material - it calls S/4HANA through an API. It can also call external systems the same way. Notice what it does NOT do: it never edits the core. That's clean core in one diagram, and it's exactly the shape of the app you'll learn to build."

TEACHING TIP: Trace the arrows with your cursor during the live session. Say the four inner layers out loud - they map directly to the CAP slides next.

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "Those four layers inside the box are the heart of CAP. Let's define it properly."
""")

# ============================================================================
# SLIDE 10 — WHAT IS CAPM
# ============================================================================
s = slide(); header(s, "SAP CAPM", "What Is SAP CAPM?", "6 min")
tb(s, Inches(0.55), Inches(1.35), Inches(12.2), Inches(1.15),
   [("The ", 17, INK, False), ("SAP Cloud Application Programming Model (CAP / CAPM)", 17, BLUE, True),
    (" is SAP's framework of languages, libraries and tools for building enterprise services and applications.",
     17, INK, False)], line_spacing=1.12)
# why bullets
tb(s, Inches(0.55), Inches(2.7), Inches(0.4), Inches(0.4), [("Why developers use it", 15, NAVY, True)])
why = [
    ("Focus on the business, not the plumbing", "CAP handles the repetitive wiring for you"),
    ("Convention over configuration", "sensible defaults - \"things just work out of the box\""),
    ("Grow as you go", "start tiny on your laptop, scale up to the cloud"),
    ("Open & standard", "JavaScript/Node.js (or Java), OData, SQL - transferable skills"),
]
yy0 = Inches(3.15)
for i, (h, d) in enumerate(why):
    yy = yy0 + Inches(0.62) * i
    ch_ = rect(s, Inches(0.6), yy + Inches(0.03), Inches(0.3), Inches(0.3), fill=TEAL, rounded=True)
    shp_text(ch_, [("✓", 13, WHITE, True)])
    tb(s, Inches(1.05), yy, Inches(6.3), Inches(0.6),
       [(h + "  -  ", 13.5, INK, True), (d, 13, GRAY_TX, False)], line_spacing=1.0,
       anchor=MSO_ANCHOR.MIDDLE)
# right callout
rect(s, Inches(7.75), Inches(2.95), Inches(5.0), Inches(3.3), fill=NAVY, rounded=True)
tb(s, Inches(8.05), Inches(3.15), Inches(4.4), Inches(0.4), [("In one line", 13, AMBER, True)])
tb(s, Inches(8.05), Inches(3.55), Inches(4.45), Inches(1.5),
   [("CAP is the fast, opinionated way to turn a data model into a secure, running business service on SAP BTP.",
     17, WHITE, True)], line_spacing=1.12)
rect(s, Inches(8.05), Inches(5.2), Inches(4.4), Pt(1.5), fill=BLUE)
tb(s, Inches(8.05), Inches(5.35), Inches(4.45), Inches(0.85),
   [("Not a replacement for SAP ERP. ", 12.5, AMBER, True),
    ("CAP builds services and apps around SAP - it is not the ERP itself.", 12.5, BLUE_LT, False)],
   line_spacing=1.08)
pagenum(s, 10)
notes(s, """
KEY MESSAGE: CAP is SAP's opinionated framework (languages + libraries + tools) for building enterprise services fast, on BTP. It is NOT the ERP and NOT a replacement for SAP.

SCRIPT: "CAP - the SAP Cloud Application Programming Model, also written CAPM - is a framework: a set of languages, libraries and tools that take you from a data model to a running, secure service with far less boilerplate. Developers like it for four reasons. It lets you focus on the business problem, not the plumbing. It favours convention over configuration - SAP's own docs say things 'just work out of the box with zero configuration'. It lets you 'grow as you go' - start on your laptop, scale to the cloud. And it's built on open standards: JavaScript and Node.js, OData, SQL - skills that transfer anywhere."

OFFICIAL PHRASING (source: cap.cloud.sap): "convention over configuration", "zero configuration", "Jumpstart & Grow as You Go".

MUST-SAY GUARDRAIL: "CAP is not the SAP ERP and it does not replace it. CAP builds services and apps that sit around SAP." This prevents a common beginner misconception.

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "Here's what's actually under the hood - the pieces and how they connect."
""")

# ============================================================================
# SLIDE 11 — CAPM ARCHITECTURE + STACK
# ============================================================================
s = slide(); header(s, "SAP CAPM", "Inside a CAP Application")
# left: layered stack
lx = Inches(0.55); lw = Inches(6.1); ly = Inches(1.45)
layers = [
    ("SAP Fiori / UI5", "the user interface (optional, pluggable)", BLUE),
    ("OData V4 / REST services", "APIs, auto-generated from your model", NAVY),
    ("Business logic (Node.js / Java)", "custom handlers, validation, events", TEAL),
    ("CDS - data model & services", "define entities once, in plain text", NAVY2),
    ("Database: SQLite (local) → SAP HANA Cloud", "persistence, same model both places", NAVY),
]
lh = Inches(0.92)
for i, (t, d, c) in enumerate(layers):
    yy = ly + (lh + Inches(0.05)) * i
    r = rect(s, lx, yy, lw, lh, fill=WHITE, line=c, line_w=1.5, rounded=True)
    rect(s, lx, yy, Inches(0.14), lh, fill=c)
    tb(s, lx + Inches(0.32), yy + Inches(0.1), lw - Inches(0.5), Inches(0.42),
       [(t, 14.5, c, True)])
    tb(s, lx + Inches(0.32), yy + Inches(0.5), lw - Inches(0.5), Inches(0.38),
       [(d, 11.5, GRAY_TX, False)])
tb(s, lx, ly + (lh + Inches(0.05)) * 5 + Inches(0.02), lw, Inches(0.35),
   [("Secured throughout by XSUAA / SAP Cloud Identity (roles & scopes)", 11.5, AMBER, True)],
   align=PP_ALIGN.CENTER)
# right: ecosystem relationships
rx = Inches(7.0)
rect(s, rx, Inches(1.45), Inches(5.78), Inches(5.3), fill=GRAY_BG, line=GRAY_MID, line_w=1, rounded=True)
tb(s, rx + Inches(0.25), Inches(1.58), Inches(5.2), Inches(0.4),
   [("How the pieces relate", 15, NAVY, True)])
rel = [
    ("CDS", "one definition → database tables AND API, automatically"),
    ("OData", "the standard API protocol SAP tools understand"),
    ("Fiori", "SAP's UI; reads the OData service with little code"),
    ("HANA Cloud", "the production database on BTP"),
    ("SAP BTP", "where the finished app is deployed and run"),
]
for i, (k, v) in enumerate(rel):
    yy = Inches(2.1) + Inches(0.7) * i
    kbox = rect(s, rx + Inches(0.25), yy, Inches(1.45), Inches(0.52), fill=BLUE, rounded=True)
    shp_text(kbox, [(k, 13, WHITE, True)])
    tb(s, rx + Inches(1.85), yy, Inches(3.7), Inches(0.55), [(v, 12.5, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
pagenum(s, 11)
notes(s, """
KEY MESSAGE: A CAP app is a clean stack - CDS model at the base, services/APIs generated from it, custom Node.js logic, an optional Fiori UI, backed by SQLite locally or HANA Cloud in the cloud, secured by XSUAA/Identity throughout.

SCRIPT: "Read the stack bottom-up. You describe your data once in CDS - Core Data Services - in plain text. From that single definition, CAP creates your database tables AND an OData service - that's the API - automatically. You add business logic in Node.js: validations, calculations, reactions to events. On top, an optional SAP Fiori UI reads that OData service with very little code. The same model runs on SQLite on your laptop and on SAP HANA Cloud in production. And security - roles and scopes via XSUAA - wraps the whole thing."

THE 'AHA': "Define your data once, and the database and the API are generated for you." That single idea is why CAP feels productive.

DELIVERY TIME: ~1.5 minutes. Point to each layer.

TRANSITION: "Let's see that as a short journey a developer actually walks - with a tiny, real example."
""")

# ============================================================================
# SLIDE 12 — CAPM LIFECYCLE + EXAMPLE + SNIPPET
# ============================================================================
s = slide(); header(s, "SAP CAPM", "A Developer's Journey: Leave-Request App")
steps = [
    ("1  Model", "Define data\nin CDS", NAVY2),
    ("2  Service", "Expose it as\nan OData API", NAVY),
    ("3  Logic", "Add validation\n& rules (Node.js)", TEAL),
    ("4  Run", "Test locally\non SQLite", BLUE),
    ("5  UI", "Add a Fiori\nscreen", BLUE),
    ("6  Deploy", "Push to\nSAP BTP", GREEN),
]
sw_ = Inches(1.93); sgap = Inches(0.08); sx0 = Inches(0.55); sy = Inches(1.5); sh_ = Inches(1.3)
for i, (t, d, c) in enumerate(steps):
    x = sx0 + (sw_ + sgap) * i
    r = rect(s, x, sy, sw_, sh_, fill=c, rounded=True)
    shp_text(r, [(t, 14, WHITE, True), (d, 10.5, BLUE_LT, False)], line_spacing=1.0)
    if i < len(steps) - 1:
        arrow(s, x + sw_ - Inches(0.02), sy + Inches(0.5), Inches(0.12), Inches(0.3), fill=GRAY_MID)
# code snippet
rect(s, Inches(0.55), Inches(3.1), Inches(6.5), Inches(3.3), fill=NAVY, rounded=True)
tb(s, Inches(0.8), Inches(3.22), Inches(6), Inches(0.35),
   [("schema.cds  -  define the data once", 12, AMBER, True), ("  (readable, not scary)", 11, BLUE_LT, False)])
code = [
    "entity LeaveRequests {",
    "  key ID      : UUID;",
    "  employee    : String;",
    "  fromDate    : Date;",
    "  toDate      : Date;",
    "  reason      : String;",
    "  status      : String default 'Pending';",
    "}",
]
tb(s, Inches(0.85), Inches(3.68), Inches(6), Inches(2.6),
   [(c, 14, WHITE, False, False, "Consolas") for c in code],
   line_spacing=1.12, space_after=1)
# explanation panel
rect(s, Inches(7.3), Inches(3.1), Inches(5.45), Inches(3.3), fill=BLUE_XLT, rounded=True)
tb(s, Inches(7.55), Inches(3.25), Inches(5), Inches(0.4), [("From those 8 lines, CAP gives you:", 13.5, NAVY, True)])
gives = [
    "A database table for leave requests",
    "A full OData API: create, read, update, delete",
    "A ready-made Fiori list & form to edit it",
    "A place to add rules (e.g. toDate ≥ fromDate)",
]
for i, g in enumerate(gives):
    yy = Inches(3.75) + Inches(0.55) * i
    rect(s, Inches(7.6), yy + Inches(0.05), Inches(0.28), Inches(0.28), fill=GREEN, rounded=True)
    tb(s, Inches(7.98), yy, Inches(4.6), Inches(0.5), [(g, 12.5, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
tb(s, Inches(7.55), Inches(6.05), Inches(5), Inches(0.35),
   [("Same pattern builds inventory, purchase-request or approval apps.", 11.5, GRAY_TX, True)])
pagenum(s, 12)
notes(s, """
KEY MESSAGE: Show the end-to-end flow with a concrete, friendly example (an employee leave-request app) and prove how little code it takes to get a lot.

SCRIPT: "Here's the journey for a simple leave-request app. Step one, model the data in CDS. Look at the snippet - eight readable lines: an ID, who's asking, the dates, a reason, a status. That's it; you don't need to understand every symbol. Step two, expose it as a service - an OData API. Step three, add logic in Node.js, like 'the end date can't be before the start date'. Step four, run it on your laptop against SQLite and test it. Step five, add a Fiori screen. Step six, deploy to BTP. From those eight lines, CAP already gives you a table, a full create-read-update-delete API, and a ready-made Fiori list and form."

REASSURANCE: "If the code looked approachable - good. That's the point. CAP removes the scary boilerplate so beginners can be productive early."

NOTE: The same pattern generalises - inventory, purchase requests, approvals.

DELIVERY TIME: ~2 minutes. This is a central slide - slow down here.

TRANSITION: "Now, the part that makes this program different from a normal SAP course: how AI changes the way you'd do every one of those steps."
""")

# ============================================================================
# SLIDE 13 — AI ACROSS THE SDLC (table)
# ============================================================================
s = slide(); header(s, "AI & the development lifecycle", "AI Across the SDLC", "4 min")
tb(s, Inches(0.55), Inches(1.3), Inches(12.2), Inches(0.4),
   [("SDLC = the stages software goes through, from idea to running system. AI can assist at each - but you stay responsible.",
     13.5, GRAY_TX, False)])
headers = ["Stage", "AI can assist with...", "CAP example", "You still own..."]
data = [
    ("Requirements", "Turn notes into user stories", "Draft stories for a leave app", "Is it correct & complete?"),
    ("Design", "Suggest a structure", "Propose entities & services", "Right architecture choice"),
    ("Data model (CDS)", "Draft the CDS", "Generate LeaveRequests entity", "Review fields & types"),
    ("Build logic", "Generate Node.js handlers", "Draft date-validation rule", "Does it match the rule?"),
    ("Testing", "Suggest test cases", "Edge cases for dates/status", "Decide what must pass"),
    ("Debug", "Explain errors & fixes", "Explain a 400 OData error", "Verify the real cause"),
    ("Docs & review", "Draft README & comments", "Summarise what a service does", "Accuracy & clarity"),
    ("Deploy & run", "Explain deploy steps/logs", "Interpret a cf deploy log", "Safe, authorised action"),
]
colx = [Inches(0.55), Inches(2.75), Inches(6.35), Inches(9.65)]
colw = [Inches(2.2), Inches(3.6), Inches(3.3), Inches(3.1)]
ty = Inches(1.85); rh = Inches(0.5)
# header row
for j, htext in enumerate(headers):
    hc = rect(s, colx[j], ty, colw[j], rh, fill=NAVY)
    shp_text(hc, [(htext, 12.5, WHITE, True)], align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)
    hc.text_frame.margin_left = Pt(8)
for i, row in enumerate(data):
    yy = ty + rh + (Inches(0.515)) * i
    band = GRAY_BG if i % 2 == 0 else WHITE
    for j, cell in enumerate(row):
        cc = rect(s, colx[j], yy, colw[j], Inches(0.515), fill=band, line=GRAY_MID, line_w=0.5)
        colr = AMBER if j == 3 else (BLUE if j == 2 else INK)
        bold = (j == 0)
        tb(s, colx[j] + Inches(0.1), yy, colw[j] - Inches(0.15), Inches(0.515),
           [(cell, 11, NAVY if j == 0 else (GRAY_TX if j == 3 else INK),
             True if j == 0 else False)], anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
pagenum(s, 13)
notes(s, """
KEY MESSAGE: AI is a capable assistant at every SDLC stage, but human judgment, validation and responsibility never transfer to the AI.

SCRIPT: "SDLC - software development life cycle - is just the stages software goes through: understand requirements, design, model data, build logic, test, debug, document, deploy. AI can help at every row. It can turn messy notes into user stories, draft your CDS model, generate a first Node.js handler, suggest test cases including nasty edge cases, explain an error message in plain English, and draft your README. But look at the last column - that's always yours. Is the requirement actually right? Is the architecture sound? Does the generated code really enforce the business rule? Is this a safe, authorised action to run?"

HONESTY: Do NOT claim AI replaces developers or guarantees speed. Say plainly: "AI drafts; you decide. It accelerates the typing, not the thinking."

DELIVERY TIME: ~1.5 minutes. Don't read all 8 rows - walk 3 and gesture at the pattern.

TRANSITION: "Here's the same idea as a before-and-after workflow, with the safety rules spelled out."
""")

# ============================================================================
# SLIDE 14 — TRADITIONAL vs AI-ASSISTED + GUARDRAILS
# ============================================================================
s = slide(); header(s, "AI & the development lifecycle", "Traditional vs AI-Assisted - Responsibly")
# two flows
tb(s, Inches(0.55), Inches(1.3), Inches(6), Inches(0.4), [("Traditional workflow", 15, GRAY_TX, True)])
trad = ["Read docs & search", "Write boilerplate by hand", "Hit an error", "Google for hours", "Repeat"]
for i, t in enumerate(trad):
    yy = Inches(1.8) + Inches(0.6) * i
    r = rect(s, Inches(0.55), yy, Inches(5.5), Inches(0.5), fill=GRAY_BG, line=GRAY_MID, line_w=1, rounded=True)
    shp_text(r, [(t, 13, INK, False)], align=PP_ALIGN.LEFT)
    r.text_frame.margin_left = Pt(12)
tb(s, Inches(6.75), Inches(1.3), Inches(6), Inches(0.4), [("AI-assisted workflow", 15, AMBER, True)])
ai = ["Describe intent to AI", "Get a first draft fast", "Review & correct it", "Ask AI to explain errors", "Ship with understanding"]
for i, t in enumerate(ai):
    yy = Inches(1.8) + Inches(0.6) * i
    r = rect(s, Inches(6.75), yy, Inches(5.5), Inches(0.5), fill=BLUE_XLT, line=BLUE, line_w=1, rounded=True)
    shp_text(r, [(t, 13, INK, True if i in (2,4) else False)], align=PP_ALIGN.LEFT)
    r.text_frame.margin_left = Pt(12)
# guardrails strip
rect(s, Inches(0.55), Inches(5.0), Inches(12.2), Inches(1.75), fill=NAVY, rounded=True)
tb(s, Inches(0.8), Inches(5.12), Inches(11.6), Inches(0.4),
   [("Non-negotiable guardrails - what we teach you to always do:", 14, AMBER, True)])
guards = [
    "Read & understand every line before you use it",
    "Validate security - never trust generated auth code blindly",
    "Never paste secrets or confidential data into a prompt",
    "Test the business logic - AI can be confidently wrong",
    "Know the concepts yourself - AI assists, it doesn't replace",
    "You sign off; you're accountable for what ships",
]
for i, g in enumerate(guards):
    col = i % 2; row = i // 2
    x = Inches(0.9) + Inches(6.0) * col
    yy = Inches(5.55) + Inches(0.38) * row
    tb(s, x, yy, Inches(0.3), Inches(0.35), [("•", 15, BLUE, True)])
    tb(s, x + Inches(0.25), yy, Inches(5.6), Inches(0.38), [(g, 12, WHITE, False)],
       anchor=MSO_ANCHOR.MIDDLE)
pagenum(s, 14)
notes(s, """
KEY MESSAGE: AI shifts the developer from typist to reviewer/decider. Benefits are real but bounded; the guardrails are the professional standard this program instils.

SCRIPT: "Left side, the old loop: read docs, write boilerplate by hand, hit an error, lose an afternoon to search. Right side, with AI: describe what you want, get a solid first draft in seconds, then - and this is the job now - review it, correct it, ask it to explain errors, and ship it because you understand it. The developer moves from typist to reviewer and decision-maker."

GUARDRAILS (say these firmly, they're the integrity of the course): understand every line; validate security; never paste secrets or confidential data into a prompt; test the business logic because AI can be confidently wrong; know the fundamentals yourself; and you sign off - you're accountable.

REALISM: "AI won't guarantee you're faster on day one, and it won't make you a developer by itself. It makes a developer who knows the fundamentals much more productive."

DELIVERY TIME: ~1.5 minutes.

TRANSITION: "Put the technology and the AI skills together and you get a genuinely employable profile. Let's talk careers."
""")

# ============================================================================
# SLIDE 15 — CAREERS + ROADMAP
# ============================================================================
s = slide(); header(s, "Careers", "Where These Skills Can Take You", "2 min")
# roles row
roles = ["SAP BTP Developer", "SAP CAP Developer", "SAP Cloud App Developer",
         "SAP Full-Stack Developer", "SAP Integration Developer", "SAP Technical Consultant"]
rw = Inches(1.97); rgap = Inches(0.05); rx0 = Inches(0.55); ry = Inches(1.4)
for i, t in enumerate(roles):
    x = rx0 + (rw + rgap) * i
    r = rect(s, x, ry, rw, Inches(0.78), fill=BLUE_XLT, line=BLUE, line_w=1, rounded=True)
    shp_text(r, [(t, 11.5, NAVY, True)], line_spacing=0.95)
tb(s, Inches(0.55), Inches(2.35), Inches(12), Inches(0.35),
   [("Example entry-level roles in the SAP BTP / CAP ecosystem", 12, GRAY_TX, True)], align=PP_ALIGN.CENTER)
# growth roadmap
tb(s, Inches(0.55), Inches(2.9), Inches(6), Inches(0.4), [("A realistic growth path", 15, NAVY, True)])
grow = [
    ("Learner", "Build guided apps;\nportfolio on GitHub", NAVY2),
    ("Junior Developer", "Ship features on a team;\nfix bugs; write tests", BLUE),
    ("Developer", "Own modules; design\nservices; mentor juniors", TEAL),
    ("Senior / Specialist", "Architecture, integration,\nsecurity, lead delivery", GREEN),
]
gw = Inches(2.9); ggap = Inches(0.2); gx0 = Inches(0.55); gy = Inches(3.4); gh = Inches(1.5)
for i, (t, d, c) in enumerate(grow):
    x = gx0 + (gw + ggap) * i
    r = rect(s, x, gy, gw, gh, fill=WHITE, line=c, line_w=1.75, rounded=True)
    rect(s, x, gy, gw, Inches(0.12), fill=c)
    tb(s, x, gy + Inches(0.22), gw, Inches(0.4), [(t, 14.5, c, True)], align=PP_ALIGN.CENTER)
    tb(s, x + Inches(0.15), gy + Inches(0.65), gw - Inches(0.3), Inches(0.8),
       [(d, 11.5, INK, False)], align=PP_ALIGN.CENTER, line_spacing=1.03)
    if i < len(grow) - 1:
        arrow(s, x + gw + Inches(0.02), gy + Inches(0.6), Inches(0.14), Inches(0.3), fill=c)
# skills + complement
rect(s, Inches(0.55), Inches(5.2), Inches(12.2), Inches(1.5), fill=GRAY_BG, line=GRAY_MID, line_w=1, rounded=True)
tb(s, Inches(0.8), Inches(5.32), Inches(5.9), Inches(1.3),
   [("Skills employers look for: ", 13, TEAL, True),
    ("JavaScript/Node.js, APIs & OData, databases/SQL, Git, cloud basics, and SAP CAP/BTP - plus the judgment to use AI well.",
     13, INK, False)], line_spacing=1.1)
tb(s, Inches(6.95), Inches(5.32), Inches(5.6), Inches(1.3),
   [("Complements classic SAP skills: ", 13, TEAL, True),
    ("CAP sits naturally alongside ABAP, UI5 and Fiori - you add the modern cloud layer to a proven ecosystem.",
     13, INK, False)], line_spacing=1.1)
pagenum(s, 15)
notes(s, """
KEY MESSAGE: These skills map to real, named roles and a believable growth path - without promising jobs, salaries or placement.

SCRIPT: "What can this become? Entry-level titles you'll actually see include SAP BTP Developer, SAP CAP Developer, Cloud Application Developer, Full-Stack Developer, Integration Developer, and Technical Consultant. A realistic path is: learner building guided apps and a GitHub portfolio, then junior developer shipping features on a team, then developer owning modules and design, then senior or specialist in architecture, integration or security. The skills behind all of it - JavaScript, APIs, databases, Git, cloud, and SAP CAP - are exactly what employers ask for, and they complement classic SAP skills like ABAP, UI5 and Fiori rather than competing with them."

HONESTY GUARDRAIL (important): Do NOT promise jobs, salaries, placement, or specific demand statistics. I deliberately kept numbers off this slide because I could not verify current, geo-specific salary/demand data in this session. If you quote figures live, cite a current, named source (e.g. a recent SAP/industry salary survey or a job-board report) and state the country and date. Say: "Demand for SAP cloud developers has been strong, but I'll point you to current sources rather than quote a number I can't verify here."

DELIVERY TIME: ~1 minute.

TRANSITION: "So how do you get from today to that first role? Through the curriculum - let's walk it."
""")

# ============================================================================
# SLIDE 16 — CURRICULUM PART 1
# ============================================================================
s = slide(); header(s, "Training curriculum", "Your Learning Journey (1 of 2)", "2 min")
tb(s, Inches(0.55), Inches(1.3), Inches(12.2), Inches(0.4),
   [("24 weeks  •  12 steps  •  each step ends with something you can show. Weeks 1-12 below.",
     13.5, GRAY_TX, True)])
c1 = [
    ("W1-2", "Programming Fundamentals", "Logic, functions, CLI, Git & GitHub", NAVY2),
    ("W3-4", "JavaScript & Web Basics", "ES6+, async, JSON, HTTP, DOM", BLUE),
    ("W5-6", "Node.js, REST & BTP Foundations", "Express API, cloud basics, BTP trial, SQL", BLUE),
    ("W7-8", "CAP Core: CDS & Services", "Domain modeling, services  →  Project 1A", TEAL),
    ("W9-10", "Custom Logic, OData & Integration", "Handlers, validation, external APIs  →  Project 1B", TEAL),
    ("W11-12", "User Interfaces with SAP Fiori", "Fiori Elements + UI5  →  Project 1 complete", GREEN),
]
cy = Inches(1.9); chh = Inches(0.72)
for i, (wk, title, body, c) in enumerate(c1):
    yy = cy + (chh + Inches(0.07)) * i
    rect(s, Inches(0.55), yy, Inches(12.2), chh, fill=WHITE, line=GRAY_MID, line_w=1, rounded=True)
    wkb = rect(s, Inches(0.55), yy, Inches(1.4), chh, fill=c, rounded=True)
    shp_text(wkb, [(wk, 14, WHITE, True)])
    tb(s, Inches(2.15), yy + Inches(0.08), Inches(5.0), Inches(0.58),
       [(title, 14.5, NAVY, True)], anchor=MSO_ANCHOR.MIDDLE)
    tb(s, Inches(7.1), yy, Inches(5.5), chh, [(body, 12.5, GRAY_TX, False)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
pagenum(s, 16)
notes(s, """
KEY MESSAGE: The first half builds from true beginnings (logic, Git) to a complete, guided CAP application with a Fiori UI (Project 1). Everything here is drawn directly from weekly_agenda.md.

SCRIPT: "The program is 24 weeks, 12 steps of two weeks each, and every step ends with something you can show. The first twelve weeks: weeks 1-2, genuine fundamentals - logic, functions, the command line, Git and GitHub. Weeks 3-4, JavaScript and how the web works. Weeks 5-6, Node.js, building a REST API, cloud concepts, and your first SAP BTP trial account. Weeks 7-8, the heart of CAP: modelling data with CDS and exposing services - that's Project 1, Part A. Weeks 9-10, custom logic, OData and integrating an external API - Part B. Weeks 11-12, you put a SAP Fiori interface on top, completing Project 1, a guided CRUD application."

FIDELITY NOTE: These milestones summarise the agenda's detailed bullets without inventing anything. Deliverables (Project 1A/1B/complete) are taken straight from the file.

DELIVERY TIME: ~45 seconds. Scan, don't read every line.

TRANSITION: "The second half takes you to production - real database, security, deployment, teamwork, testing with AI, and a capstone."
""")

# ============================================================================
# SLIDE 17 — CURRICULUM PART 2 + OUTCOMES
# ============================================================================
s = slide(); header(s, "Training curriculum", "Your Learning Journey (2 of 2)")
c2 = [
    ("W13-14", "Databases & SAP HANA Cloud", "Advanced SQL, HANA Cloud, performance", NAVY2),
    ("W15-16", "Auth, Authorization & Security", "XSUAA, roles & scopes, OWASP, GDPR awareness", BLUE),
    ("W17-18", "Deployment, MTA & BTP Services", "Cloud Foundry, deploy, Work Zone launchpad", BLUE),
    ("W19-20", "Team Project", "User stories, PRs, code review  →  Project 2", TEAL),
    ("W21-22", "Testing, CI/CD & AI Tools", "Jest, GitHub Actions, AI assistants & prompting", AMBER),
    ("W23-24", "Capstone Project", "Design→deploy end-to-end  →  Project 3 + demo", GREEN),
]
cy = Inches(1.5); chh = Inches(0.62)
for i, (wk, title, body, c) in enumerate(c2):
    yy = cy + (chh + Inches(0.06)) * i
    rect(s, Inches(0.55), yy, Inches(12.2), chh, fill=WHITE, line=GRAY_MID, line_w=1, rounded=True)
    wkb = rect(s, Inches(0.55), yy, Inches(1.4), chh, fill=c, rounded=True)
    shp_text(wkb, [(wk, 13.5, WHITE, True)])
    tb(s, Inches(2.15), yy, Inches(5.0), chh, [(title, 14, NAVY, True)], anchor=MSO_ANCHOR.MIDDLE)
    tb(s, Inches(7.1), yy, Inches(5.5), chh, [(body, 12, GRAY_TX, False)], anchor=MSO_ANCHOR.MIDDLE)
# outcomes strip
rect(s, Inches(0.55), Inches(5.7), Inches(12.2), Inches(1.05), fill=NAVY, rounded=True)
tb(s, Inches(0.8), Inches(5.8), Inches(3.4), Inches(0.9),
   [("You finish able to:", 14, AMBER, True)], anchor=MSO_ANCHOR.MIDDLE)
outs = ["Build & deploy a real CAP app on SAP BTP",
        "Model data, write logic, secure & test it",
        "Show 3 projects + a capstone on GitHub"]
for i, o in enumerate(outs):
    x = Inches(3.3) + Inches(3.18) * i
    tb(s, x, Inches(5.82), Inches(0.3), Inches(0.9), [("✓", 14, GREEN, True)], anchor=MSO_ANCHOR.MIDDLE)
    tb(s, x + Inches(0.3), Inches(5.82), Inches(2.9), Inches(0.9), [(o, 12, WHITE, False)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
pagenum(s, 17)
notes(s, """
KEY MESSAGE: The second half is production reality - database, security, deployment, real teamwork, testing with CI/CD and AI tooling - ending in a deployed capstone and portfolio.

SCRIPT: "Weeks 13-14, a real cloud database with SAP HANA Cloud. Weeks 15-16, security done properly - authentication and authorisation, roles and scopes, an OWASP overview, GDPR awareness. Weeks 17-18, deployment: Cloud Foundry, and publishing an app tile to a Work Zone launchpad. Weeks 19-20, a team project - user stories, pull requests, code reviews - that's Project 2. Weeks 21-22, testing and CI/CD with GitHub Actions, and this is where AI tools are taught explicitly: responsible use of AI coding assistants and prompt engineering for CAP and CDS. Weeks 23-24, the capstone: you design, build, test and deploy an end-to-end application, Project 3, and present it."

AI PLACEMENT (be precise): The agenda names AI explicitly in weeks 21-22 (AI coding assistants - Joule for Developers, GitHub Copilot, Claude - and prompt engineering, plus SAP AI Core/Generative AI Hub awareness). Elsewhere in the webinar we show AI across the whole SDLC as a working practice; on stage, distinguish "formally in the syllabus here" from "a practice we encourage throughout."

OUTCOMES are taken from the file's deliverables: a deployed capstone (Project 3), three projects, documentation and portfolio.

DELIVERY TIME: ~45 seconds.

TRANSITION: "Enough slides about building - let me actually build something in front of you."
""")

# ============================================================================
# SLIDE 18 — DEMO INTRO
# ============================================================================
s = slide(); bg(s, NAVY)
rect(s, 0, 0, Inches(0.18), SH, fill=BLUE)
chip_ = rect(s, Inches(0.9), Inches(0.95), Inches(2.3), Inches(0.6), fill=BLUE, rounded=True)
shp_text(chip_, [("LIVE DEMO  •  10 MIN", 14, WHITE, True)])
tb(s, Inches(0.9), Inches(1.85), Inches(11.5), Inches(1.0),
   [("Let's Build a CAP Service - Live", 38, WHITE, True)], font=FONTSB)
tb(s, Inches(0.9), Inches(2.95), Inches(11.5), Inches(0.5),
   [("A tiny Leave-Request service, from empty folder to a working API - with AI helping.",
     17, BLUE_LT, False)])
goals = [
    "See how fast an idea becomes a running service",
    "Watch CDS turn into a database + API automatically",
    "See AI draft a validation and explain an error",
    "Prove it works by calling the live API in the browser",
]
for i, g in enumerate(goals):
    yy = Inches(3.9) + Inches(0.6) * i
    rect(s, Inches(0.95), yy + Inches(0.06), Inches(0.3), Inches(0.3), fill=AMBER, rounded=True)
    tb(s, Inches(1.4), yy, Inches(10.5), Inches(0.5), [(g, 16, WHITE, False)], anchor=MSO_ANCHOR.MIDDLE)
tb(s, Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.5),
   [("This is a real, live demo - not screenshots. If the environment misbehaves, that's part of the lesson.",
     13, GRAY_MID, True, True)])
pagenum(s, 18)
notes(s, """
KEY MESSAGE: Set expectations for a genuine live build; keep it small and meaningful; make the payoff ("look how little produced so much") land.

SCRIPT: "Slides off - let's build. In the next ten minutes I'll create a small leave-request service from an empty folder to a working API, and I'll use an AI assistant along the way. Watch for three things: how fast an idea becomes a running service, how a few lines of CDS become a database and an API with no extra work, and how AI drafts a validation rule and explains an error - while I stay in control and check its work."

FALLBACK PLAN (critical - rehearse this):
1) If 'cds watch' or npm fails: switch to a pre-created project folder already scaffolded (keep one ready).
2) If no internet / BTP unreachable: run everything LOCALLY on SQLite - the demo is designed to need nothing but Node.js and cds-dk installed beforehand.
3) If the whole machine fails: play a 2-minute pre-recorded screen capture (keep it on the desktop) and narrate it, clearly stating it's a recording.
4) If AI tool is unavailable: paste a pre-saved prompt+response from a text file and explain what it would have done.
Always have the finished project zipped locally as the ultimate backup.

PRE-FLIGHT CHECKLIST (before the webinar): Node.js LTS + @sap/cds-dk installed; 'cds --version' works; empty demo folder ready; pre-scaffolded fallback folder ready; recording on desktop; font size in terminal/editor turned up; close notifications.

DELIVERY TIME: ~30 seconds, then switch to the live environment.

TRANSITION: "Here's exactly the sequence I'll follow."
""")

# ============================================================================
# SLIDE 19 — DEMO FLOW
# ============================================================================
s = slide(); header(s, "Live demo", "The 10-Minute Flow")
flow = [
    ("1", "Scaffold", "cds init leave-app\nand open it", "~1 min", NAVY2),
    ("2", "Model (CDS)", "Define LeaveRequests\nentity in a .cds file", "~2 min", NAVY),
    ("3", "Service", "Expose it; run\ncds watch (SQLite)", "~2 min", TEAL),
    ("4", "Call the API", "Open the OData URL;\ncreate & read a record", "~2 min", BLUE),
    ("5", "AI assist", "AI drafts a date-check\n& explains an error", "~2 min", AMBER),
]
fw = Inches(2.35); fgap = Inches(0.1); fx0 = Inches(0.55); fy = Inches(1.7); fh = Inches(2.6)
for i, (n, t, d, mins, c) in enumerate(flow):
    x = fx0 + (fw + fgap) * i
    rect(s, x, fy, fw, fh, fill=WHITE, line=c, line_w=1.75, rounded=True)
    num = rect(s, x + fw/2 - Inches(0.35), fy + Inches(0.25), Inches(0.7), Inches(0.7), fill=c, rounded=True)
    shp_text(num, [(n, 22, WHITE, True)])
    tb(s, x, fy + Inches(1.05), fw, Inches(0.4), [(t, 15, c, True)], align=PP_ALIGN.CENTER)
    tb(s, x + Inches(0.12), fy + Inches(1.5), fw - Inches(0.24), Inches(0.75),
       [(d, 12, INK, False)], align=PP_ALIGN.CENTER, line_spacing=1.05)
    mb = rect(s, x + Inches(0.5), fy + Inches(2.15), fw - Inches(1.0), Inches(0.35), fill=GRAY_BG, rounded=True)
    shp_text(mb, [(mins, 11.5, GRAY_TX, True)])
    if i < len(flow) - 1:
        arrow(s, x + fw - Inches(0.01), fy + Inches(1.1), Inches(0.12), Inches(0.3), fill=c)
rect(s, Inches(0.55), Inches(4.65), Inches(12.2), Inches(1.9), fill=BLUE_XLT, rounded=True)
tb(s, Inches(0.8), Inches(4.8), Inches(11.6), Inches(0.4), [("What the audience should take away", 15, NAVY, True)])
takes = [
    "From zero to a live API in minutes - no heavy setup",
    "CDS defines data once; database + OData come free",
    "AI speeds the draft; the developer verifies and decides",
    "This is the exact pattern you'll practise from Week 7",
]
for i, t in enumerate(takes):
    col = i % 2; row = i // 2
    x = Inches(0.95) + Inches(6.0) * col
    yy = Inches(5.3) + Inches(0.55) * row
    rect(s, x, yy + Inches(0.05), Inches(0.26), Inches(0.26), fill=TEAL, rounded=True)
    tb(s, x + Inches(0.36), yy, Inches(5.5), Inches(0.5), [(t, 13, INK, False)], anchor=MSO_ANCHOR.MIDDLE)
pagenum(s, 19)
notes(s, """
KEY MESSAGE: A tight, five-step, ten-minute script that a beginner can follow, ending with a visible, working API and a responsible AI moment.

DEMO SCRIPT (the presenter's actual commands):
1) SCAFFOLD (~1 min): 'cds init leave-app' then open in VS Code / Business Application Studio. Show the generated folders (db, srv, app).
2) MODEL (~2 min): in db/schema.cds add:
   namespace hr;
   entity LeaveRequests { key ID: UUID; employee: String; fromDate: Date; toDate: Date; reason: String; status: String default 'Pending'; }
3) SERVICE (~2 min): in srv/service.cds add:
   using hr from '../db/schema';
   service LeaveService { entity Requests as projection on hr.LeaveRequests; }
   Run 'cds watch'. Point out it auto-creates an in-memory/SQLite DB and an OData service with zero config.
4) CALL THE API (~2 min): open http://localhost:4004 ; open the $metadata and the LeaveService; POST a record via REST Client (or the UI); GET it back. The data is really there.
5) AI ASSIST (~2 min): ask the AI assistant to "write a CAP Node.js before-CREATE handler that rejects a LeaveRequest where toDate is before fromDate." Paste into srv/service.js, show it working by sending a bad request and getting a clean error. Then deliberately introduce a small error, paste the message into the AI, and have it explain the fix. Emphasise: "I read it, I understood it, I accepted it - the AI didn't decide, I did."

FALLBACK: see previous slide's notes (pre-scaffolded folder, local SQLite only, recorded clip, pre-saved AI transcript, zipped finished project).

TIMEBOX DISCIPLINE: if any step runs long, skip the Fiori UI entirely - the API in the browser is enough proof. Keep a hard stop at 10 minutes so Q&A is protected.

DELIVERY TIME: 10 minutes total (this slide ~30 sec to preview, rest is live).

TRANSITION (after demo): "That's the whole loop in miniature. Let's bring it together and open it up to your questions."
""")

# ============================================================================
# SLIDE 20 — Q&A + RECAP
# ============================================================================
s = slide(); bg(s, WHITE)
rect(s, 0, 0, SW, Inches(1.18), fill=NAVY)
rect(s, 0, Inches(1.18), SW, Pt(3), fill=BLUE)
tb(s, Inches(0.55), Inches(0.3), Inches(10), Inches(0.66), [("Questions & Recap", 26, WHITE, True)],
   font=FONTSB, anchor=MSO_ANCHOR.MIDDLE)
chip_ = rect(s, Inches(11.3), Inches(0.33), Inches(1.5), Inches(0.52), fill=BLUE, rounded=True)
shp_text(chip_, [("Q&A  •  10 MIN", 12.5, WHITE, True)])
# the story chain
tb(s, Inches(0.55), Inches(1.45), Inches(12), Inches(0.4), [("The journey, in one line", 15, NAVY, True)])
chain = ["Business problem", "ERP", "SAP", "Cloud / BTP", "CAPM", "AI-assisted dev", "Career"]
cw = Inches(1.6); cgap = Inches(0.13); cx0 = Inches(0.55); cy = Inches(1.95)
cols = [RED, NAVY2, NAVY, BLUE, TEAL, AMBER, GREEN]
for i, (t, c) in enumerate(zip(chain, cols)):
    x = cx0 + (cw + cgap) * i
    r = rect(s, x, cy, cw, Inches(0.75), fill=c, rounded=True)
    shp_text(r, [(t, 11.5, WHITE, True)], line_spacing=0.95)
    if i < len(chain) - 1:
        arrow(s, x + cw - Inches(0.02), cy + Inches(0.23), Inches(0.14), Inches(0.28), fill=GRAY_MID)
# prompts for Q&A
rect(s, Inches(0.55), Inches(3.1), Inches(6.0), Inches(3.5), fill=GRAY_BG, line=GRAY_MID, line_w=1, rounded=True)
tb(s, Inches(0.8), Inches(3.25), Inches(5.5), Inches(0.4), [("Great questions to get us started", 14, NAVY, True)])
qs = [
    "Do I need prior SAP or coding experience?",
    "Is CAP JavaScript, Java, or both?",
    "How is this different from learning ABAP?",
    "Can I really run all this for free while learning?",
    "How exactly do you teach AI responsibly?",
    "What will my portfolio look like at the end?",
]
for i, q in enumerate(qs):
    yy = Inches(3.75) + Inches(0.46) * i
    tb(s, Inches(0.85), yy, Inches(0.3), Inches(0.4), [("?", 15, BLUE, True)])
    tb(s, Inches(1.2), yy, Inches(5.1), Inches(0.42), [(q, 12.5, INK, False)], anchor=MSO_ANCHOR.MIDDLE)
# key takeaways
rect(s, Inches(6.75), Inches(3.1), Inches(6.0), Inches(3.5), fill=NAVY, rounded=True)
tb(s, Inches(7.0), Inches(3.25), Inches(5.5), Inches(0.4), [("Three things to remember", 14, AMBER, True)])
tks = [
    ("SAP is everywhere", "huge, durable demand for people who build on it"),
    ("CAP makes it learnable", "model once; database + API come free"),
    ("AI amplifies fundamentals", "it drafts; you understand, verify and decide"),
]
for i, (h, d) in enumerate(tks):
    yy = Inches(3.8) + Inches(0.85) * i
    rect(s, Inches(7.0), yy + Inches(0.05), Inches(0.3), Inches(0.3), fill=BLUE, rounded=True)
    shp_text(rect(s, Inches(7.0), yy + Inches(0.05), Inches(0.3), Inches(0.3), fill=BLUE, rounded=True),
             [(str(i+1), 13, WHITE, True)])
    tb(s, Inches(7.45), yy, Inches(5.1), Inches(0.8),
       [(h + "  -  ", 13.5, WHITE, True), (d, 12.5, BLUE_LT, False)], line_spacing=1.05)
pagenum(s, 20)
notes(s, """
KEY MESSAGE: Recap the whole story in one chain, then hand the floor to the audience with warm, pre-seeded questions so the room isn't silent.

SCRIPT: "Let's land the story in one line: businesses had a problem - disconnected systems. ERP solved it. SAP is the leading ERP. Modern building happens in the cloud on SAP BTP. CAP is how you build there. AI makes you more productive at it. And that combination opens real careers. Three things to remember: SAP is everywhere, so demand is durable; CAP makes it genuinely learnable because you model once and get the database and API for free; and AI amplifies fundamentals - it drafts, you understand, verify and decide. Now - your turn. Here are a few questions to start us off, but I'd love yours."

FACILITATION TIPS: If chat is quiet, answer one seeded question yourself to prime the pump. Repeat each question aloud before answering (remote attendees may not hear the asker). Keep answers under ~90 seconds; park deep technical ones for after. Watch the clock - hold ~1 minute for the closing slide.

ANTICIPATED ANSWERS (brief):
- Prior experience? Basic programming logic helps; no SAP needed - the first weeks build fundamentals.
- JS or Java? CAP supports both Node.js and Java; this program uses Node.js/JavaScript.
- Vs ABAP? CAP is the modern cloud-native path and complements ABAP; both have value.
- Free while learning? BTP has trial and free-tier options, and everything runs locally on SQLite for learning (confirm current SAP trial/free-tier terms before promising).
- AI responsibly? See the guardrails slide; taught explicitly in weeks 21-22.

DELIVERY TIME: opens the 10-minute Q&A.

TRANSITION: "As we wrap, here's how to take the next step if this is for you."
""")

# ============================================================================
# SLIDE 21 — CLOSING / CTA
# ============================================================================
s = slide(); bg(s, NAVY)
rect(s, 0, 0, Inches(0.18), SH, fill=BLUE)
for i, (dx, col) in enumerate([(0, BLUE), (0.55, TEAL), (1.1, AMBER)]):
    rect(s, Inches(11.1 + dx), Inches(0.55), Inches(0.42), Inches(0.42), fill=col, rounded=True)
tb(s, Inches(0.9), Inches(1.15), Inches(11), Inches(0.5), [("YOUR NEXT STEP", 15, BLUE_LT, True)], font=FONTSB)
tb(s, Inches(0.9), Inches(1.7), Inches(11.6), Inches(1.4),
   [("Start Building on SAP BTP", 42, WHITE, True),
    ("with CAP and AI", 42, WHITE, True)], font=FONTSB, line_spacing=1.02)
# next steps cards
nexts = [
    ("1  Explore", "Review the full\n24-week curriculum"),
    ("2  Try it", "Set up a free BTP trial\nand run today's demo"),
    ("3  Connect", "Bring questions to\nour team"),
]
nw = Inches(3.65); ngap = Inches(0.25); nx0 = Inches(0.9); ny = Inches(3.55); nh = Inches(1.5)
for i, (t, d) in enumerate(nexts):
    x = nx0 + (nw + ngap) * i
    rect(s, x, ny, nw, nh, fill=NAVY2, line=BLUE, line_w=1.25, rounded=True)
    tb(s, x + Inches(0.25), ny + Inches(0.2), nw - Inches(0.5), Inches(0.45),
       [(t, 17, WHITE, True)])
    tb(s, x + Inches(0.25), ny + Inches(0.72), nw - Inches(0.5), Inches(0.7),
       [(d, 13, BLUE_LT, False)], line_spacing=1.05)
# placeholders row
rect(s, Inches(0.9), Inches(5.35), Inches(11.55), Inches(1.15), fill=NAVY2, rounded=True)
tb(s, Inches(1.15), Inches(5.45), Inches(11), Inches(0.35),
   [("Program details (to confirm):", 12.5, AMBER, True)])
ph = "Start date: [TBD]   •   Duration: 24 weeks   •   Format: [TBD]   •   Fees: [TBD]   •   Register: [LINK]   •   Contact: [EMAIL]"
tb(s, Inches(1.15), Inches(5.82), Inches(11), Inches(0.6),
   [(ph, 13, WHITE, True)], line_spacing=1.1)
tb(s, Inches(0.9), Inches(6.75), Inches(11.5), Inches(0.35),
   [("Placeholders only - no fees, dates, certifications or placement outcomes are promised here.",
     10.5, GRAY_MID, False, True)])
pagenum(s, 21)
notes(s, """
KEY MESSAGE: Clear, honest call to action with three concrete next steps and clearly-marked placeholders for anything we can't promise.

SCRIPT: "If this is for you, three next steps. One, explore the full 24-week curriculum so you can see exactly what you'd learn. Two, try it yourself - set up a free SAP BTP trial and run the little demo we just did; nothing beats building. Three, connect with us and bring your questions. On screen are the program details - and I want to be straight with you: the start date, format, fees and registration link are placeholders here. We're not promising a certificate, a salary or a job. What we're offering is a serious, structured path to real, in-demand skills."

INTEGRITY GUARDRAIL: Do NOT invent registration links, fees, batch dates, certifications, academy credentials, or placement guarantees. Replace the [TBD]/[LINK]/[EMAIL] placeholders with verified details before presenting, or leave them visibly marked as to-be-confirmed.

CLOSE WARMLY: Thank them for their time and attention; invite them to stay for any final questions.

DELIVERY TIME: ~1 minute (within the Q&A block).
""")

# ============================================================================
# SLIDE 22 — REFERENCES
# ============================================================================
s = slide(); header(s, "Appendix", "Sources & Notes")
refs = [
    ("SAP CAP official docs", "cap.cloud.sap - definition, \"convention over configuration\", \"zero configuration\", \"grow as you go\", OData/CDS, Node.js & Java, SQLite→HANA."),
    ("SAP BTP capabilities", "SAP Business Technology Platform product pages - app dev & automation, integration, data & analytics, AI (SAP AI Core / Generative AI Hub)."),
    ("SAP company facts", "Founded 1972; HQ Walldorf, Germany; world's largest enterprise-software vendor; ~110,000 employees (2025). Per SAP corporate materials / encyclopaedic summaries."),
    ("\"98 of the 100 largest companies\"", "Widely-cited SAP customer figure - verify current wording on SAP's site before quoting on stage."),
    ("SAP S/4HANA & Fiori", "SAP product documentation for S/4HANA (ERP) and SAP Fiori design guidelines."),
    ("Curriculum", "Derived directly from the program's weekly_agenda.md (24 weeks / 12 steps / Projects 1-3)."),
    ("Careers & salary data", "NOT quoted here - verify role demand & salary with a current, named, geo-specific source (e.g. recent industry salary survey or job-board report) before presenting."),
]
y = Inches(1.5)
for i, (k, v) in enumerate(refs):
    yy = y + Inches(0.76) * i
    rect(s, Inches(0.55), yy, Inches(3.4), Inches(0.66), fill=BLUE_XLT, line=BLUE, line_w=1, rounded=True)
    tb(s, Inches(0.7), yy, Inches(3.15), Inches(0.66), [(k, 12.5, NAVY, True)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
    tb(s, Inches(4.15), yy, Inches(8.6), Inches(0.66), [(v, 11.5, INK, False)],
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
tb(s, Inches(0.55), Inches(6.85), Inches(12), Inches(0.3),
   [("Facts shown as SAP/third-party claims are attributed; illustrative scenarios (NorthWind, supplier onboarding) are labelled and not real customers.",
     10, GRAY_TX, False, True)])
pagenum(s, 22)
notes(s, """
KEY MESSAGE: Transparency about sources and a reminder of what must be verified before the live delivery.

PRESENTER CHECKLIST before going live:
- Confirm SAP company facts and the '98 of 100' wording on SAP's current site.
- Confirm current SAP BTP trial / free-tier terms before telling the audience it's free.
- Do NOT add salary or job-demand numbers unless you have a current, named, geo-specific source; state country and date if you do.
- Keep illustrative examples (NorthWind Retail, supplier onboarding, leave-request app) clearly labelled as illustrative.

VERIFIED IN PREP (this session): CAP docs phrasing (cap.cloud.sap); SAP founded 1972 / Walldorf / world's largest enterprise software vendor / ~110,000 employees (2025). The '98 of 100 largest companies' figure is widely reported and attributed to SAP; verify exact current wording.
""")

prs.save("SAP_BTP_CAPM_AI_Webinar.pptx")
print("Saved SAP_BTP_CAPM_AI_Webinar.pptx with", len(prs.slides._sldIdLst), "slides")
