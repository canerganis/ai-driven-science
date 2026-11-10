"""Experimental reference data, entered by hand. Every block names its source."""

# Room temperature single crystal elastic constants (GPa): C11, C12, C44.
# Source: G. Simmons and H. Wang, Single Crystal Elastic Constants and
# Calculated Aggregate Properties (MIT Press, 1971), standard handbook values.
ELASTIC_EXP = {
    "Al": ("fcc", 108.0, 62.0, 28.3),
    "Cu": ("fcc", 168.0, 121.0, 75.4),
    "Ni": ("fcc", 247.0, 153.0, 122.0),
    "Ag": ("fcc", 124.0, 93.4, 46.1),
    "Au": ("fcc", 192.0, 163.0, 42.0),
    "Pd": ("fcc", 227.0, 176.0, 71.7),
    "Pt": ("fcc", 347.0, 251.0, 76.5),
    "Fe": ("bcc", 230.0, 135.0, 117.0),
    "Cr": ("bcc", 348.0, 67.0, 100.0),
    "Mo": ("bcc", 465.0, 163.0, 109.0),
    "W": ("bcc", 523.0, 203.0, 160.0),
    "V": ("bcc", 230.0, 120.0, 43.1),
    "Nb": ("bcc", 247.0, 135.0, 28.7),
    "Ta": ("bcc", 266.0, 158.0, 87.0),
}
