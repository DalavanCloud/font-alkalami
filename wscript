#!/usr/bin/python
# encoding: utf8
# this is a smith configuration file

# set the default output folders
out = "results"
DOCDIR = ["documentation", "web"]
OUTDIR = "installers"
ZIPDIR = "releases"
TESTDIR = "tests"
TESTRESULTSDIR = "tests"
STANDARDS = "tests/previous"

# set the version control system
VCS = 'git'

# set the product name
APPNAME = "Alkalami"

# set licensing and description

COPYRIGHT = "Copyright (c) 2015-2018, SIL International (http://www.sil.org) with Reserved Font Names Alkalami and SIL."
LICENSE = 'OFL.txt'
RESERVEDOFL = 'Alkalami, SIL'

DESC_NAME = "Alkalami"
DESC_SHORT = "Font for Arabic-based writing systems in the Kano region."
DESC_LONG = """
Alkalami is a Unicode font for the variant of the Arabic script used in the Kano region (Niger and Nigeria).

Alkalami is the local word for the Arabic "qalam", a type of sharpened stick used
for writing on wooden boards in the Kano region of Nigeria and in Niger, and what
gives the style its distinct appearance.

The baseline stroke is very thick and solid. The ascenders and other vertical strokes including the teeth are very
narrow when compared to the baseline. A generous line height is necessary to
allow for deep swashes and descenders, and the overall look of the page is a very
black, solid rectangle. Diacritics are much smaller in scale, with very little
distance from the main letters.
See http://software.sil.org/alkalami

Font sources are published and a open workflow is used for building, testing and releasing.
"""

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/Alkalami-Regular.ufo')

# set the build and test parameters

# Notes about DS variables:
#   The phrase '${DS:FILENAME_BASE}' references the instance UFO filename (from the
#   designspace file), i.e., "Alkalami-Light" or "Alkalami-Regular".
#   At present it isn't possible to reference the instance UFOs or anything in them. 
#   This code assumes the filenames of the master and instances UFOs are the same,
#   thus the phrase 'source/${DS:FILENAME_BASE}.ufo' references the master UFO
#   corresponding to the instance being built.
designspace('source/Alkalami.designspace',
    params = '-l ${DS:FILENAME_BASE}_createintance.log',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('${PSFCHANGETTFGLYPHNAMES} ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo']),
        cmd('${TYPETUNER} -o ${TGT} add ${SRC} ${DEP}', 'source/typetuner/feat_all.xml'),
        cmd('${TTFAUTOHINT} -n -c  -D arab -W ${DEP} ${TGT}')
    ),
    ap = '${DS:FILENAME_BASE}.xml',
    opentype = fea('source/${DS:FILENAME_BASE}.ufo/features.fea', no_make = 1),
    license = ofl('Alkalami', 'SIL'),
    script = ['arab'],
    version = VERSION,
    fret = fret(params='-r -oi'),
    woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v '+VERSION +' -m ../source/Alkalami-WOFF-metadata.xml'),
    typetuner='source/typetuner/feat_all.xml')


def configure(ctx):
    ctx.find_program('ttfautohint')
    ctx.find_program('typetuner')
    ctx.find_program('psfchangettfglyphnames')
