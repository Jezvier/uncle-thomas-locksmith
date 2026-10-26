"""
Line icons used across the site (instead of emoji, which look different on every
phone). 24x24 viewBox, drawn with currentColor so CSS sets the colour.
Use: icons.svg("safe") or icons.svg("star", cls="bi", fill=True)
"""

PATHS = {
    "door":     '<path d="M6 21V4.5A1.5 1.5 0 0 1 7.5 3h9A1.5 1.5 0 0 1 18 4.5V21"/><path d="M3.5 21h17"/><path d="M14.5 12.5h.01"/>',
    "keypad":   '<rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M10 7h.01M14 7h.01M10 11h.01M14 11h.01M10 15h.01M14 15h.01"/><path d="M11 18.5h2"/>',
    "wrench":   '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.4-3.4a6 6 0 0 1-7.9 7.9l-6.4 6.4a2.1 2.1 0 0 1-3-3l6.4-6.4a6 6 0 0 1 7.9-7.9z"/>',
    "safe":     '<rect x="3.5" y="3.5" width="17" height="15" rx="2"/><circle cx="12" cy="11" r="3.5"/><path d="M12 7.5V9M12 13v1.5M8.5 11H10M14 11h1.5"/><path d="M6.5 18.5V21M17.5 18.5V21"/>',
    "car":      '<path d="M4 16.5V12l1.8-4.6A2 2 0 0 1 7.7 6h8.6a2 2 0 0 1 1.9 1.4L20 12v4.5"/><path d="M3 16.5h18"/><path d="M4.5 12h15"/><circle cx="7.5" cy="16.5" r="1.8"/><circle cx="16.5" cy="16.5" r="1.8"/>',
    "lock":     '<rect x="4" y="10.5" width="16" height="11" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/><path d="M12 15v2.5"/>',
    "mailbox":  '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/>',
    "building": '<rect x="5" y="2.5" width="14" height="19" rx="1"/><path d="M9 6.5h.01M15 6.5h.01M9 10.5h.01M15 10.5h.01M9 14.5h.01M15 14.5h.01"/><path d="M10.5 21.5v-3h3v3"/>',
    "clock":    '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "tag":      '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "shield":   '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "idcard":   '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.5-1.4 1.7-2 3-2s2.5.6 3 2"/><path d="M14.5 10h4M14.5 13h3"/>',
    "check":    '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>',
    "award":    '<circle cx="12" cy="9" r="5.5"/><path d="M8.6 13.4L7 21l5-2.8 5 2.8-1.6-7.6"/>',
    "key":      '<circle cx="7.5" cy="15.5" r="4"/><path d="M10.5 12.5L20 3M16 7l2.5 2.5M14 9l2 2"/>',
    "star":     '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
}


def svg(name, cls="ico-svg", fill=False):
    body = PATHS[name]
    paint = 'fill="currentColor" stroke="none"' if fill else 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg class="{cls}" viewBox="0 0 24 24" {paint} aria-hidden="true">{body}</svg>'
