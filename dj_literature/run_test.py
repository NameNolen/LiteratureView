import random
import re
import string

ris_path = 'D:\\gitspace\\LiteratureView\\tests\\Exported_Items\\Exported_Items.ris'

woktag = "^[A-Z][A-Z0-9] |^ER$|^EF$"
ristag = "^[A-Z][A-Z0-9]  - "
riscounter = "^[0-9]+."

wokpat = re.compile(woktag)
rispat = re.compile(ristag)
riscounterpat = re.compile(riscounter)

ris_boundtags = ('TY', 'ER')
wok_boundtags = ('PT', 'ER')

wok_ignoretags = ['FN', 'VR', 'EF']
ris_ignoretags = []

TYPE_OF_REFERENCE_MAPPING = {
    "ABST": "journalArticle",
    "ADVS": "film",
    # how can we handle "database" citations?,
    "AGGR": "document",
    "ANCIENT": "document",
    "ART": "artwork",
    "BILL": "bill",
    "BLOG": "blogPost",
    "BOOK": "book",
    "CASE": "case",
    "CHAP": "bookSection",
    "CHART": "artwork",
    "CLSWK": "book",
    "COMP": "computerProgram",
    "CONF": "conferencePaper",
    "CPAPER": "conferencePaper",
    "CTLG": "magazineArticle",
    # dataset
    "DATA": "document",
    # database
    "DBASE": "document",
    "DICT": "dictionaryEntry",
    "EBOOK": "book",
    "ECHAP": "bookSection",
    "EDBOOK": "book",
    "EJOUR": "journalArticle",
    "ELEC": "webpage",
    "ENCYC": "encyclopediaArticle",
    # what's a good way to handle this?
    "EQUA": "document",
    "FIGURE": "artwork",
    "GEN": "journalArticle",
    "GOVDOC": "report",
    "GRNT": "document",
    "HEAR": "hearing",
    "ICOMM": "email",
    "INPR": "manuscript",
    "JFULL": "journalArticle",
    "JOUR": "journalArticle",
    # is this what they mean?
    "LEGAL": "case",
    "MANSCPT": "manuscript",
    "MAP": "map",
    "MGZN": "magazineArticle",
    "MPCT": "film",
    # maybe?
    "MULTI": "videoRecording",
    "MUSIC": "audioRecording",
    "NEWS": "newspaperArticle",
    "PAMP": "manuscript",
    "PAT": "patent",
    "PCOMM": "letter",
    "RPRT": "report",
    "SER": "book",
    "SLIDE": "presentation",
    # consider MUSIC
    "SOUND": "audioRecording",
    "STAND": "report",
    "STAT": "statute",
    "THES": "thesis",
    "UNBILL": "manuscript",
    "UNPD": "manuscript",
    "VIDEO": "videoRecording",
    # not in spec but used by EndNote
    "WEB": "webpage",
}


def readris(bibliography_file, wok=False):
    """Parse a ris file and return a list of entries.
    Entries are codified as dictionaries whose keys are the
    different tags. For single line and singly ocurring tags,
    the content is codified as a string. In the case of multiline
    or multiple key ocurrences, the content is returned as a list
    of strings.
    Keyword arguments:
    bibliography_file -- ris filehandle
    wok -- flag, Web of Knowledge format is used if True, otherwise
           Refman's RIS specifications are used.
    """
    ignored_lines = []
    typemapping = TYPE_OF_REFERENCE_MAPPING
    if wok:
        gettag = lambda line: line[0:2]
        getcontent = lambda line: line[2:].strip()
        istag = lambda line: (wokpat.match(line) is not None)
        starttag, endtag = wok_boundtags
        ignoretags = wok_ignoretags
    else:
        gettag = lambda line: line[0:2]
        getcontent = lambda line: line[6:].strip()
        istag = lambda line: (rispat.match(line) is not None)
        iscounter = lambda line: (riscounterpat.match(line) is not None)
        starttag, endtag = ris_boundtags
        ignoretags = ris_ignoretags

    filelines = bibliography_file.readlines()
    # Corrects for BOM in utf-8 encodings while keeping an 8-bit
    # string representation
    st = filelines[0]
    if (st[0], st[1], st[2]) == ('\xef', '\xbb', '\xbf'):
        filelines[0] = st[3:]

    inref = False
    tag = None
    current = {}
    ln = 0

    for line in filelines:
        ln += 1
        if istag(line):
            tag = gettag(line)
            if tag in ignoretags:
                continue
            elif tag == endtag:
                # Close the active entry and yield it
                yield current
                current = {}
                inref = False
            elif tag == starttag:
                # New entry
                if inref:
                    text = "Missing end of record tag in line %d:\n %s" % (
                        ln, line)
                    raise IOError(text)
                # Get ItemType
                itemtype = typemapping[getcontent(line)]
                current['itemtype'] = itemtype
                inref = True
            else:
                if not inref:
                    text = "Invalid start tag in line %d:\n %s" % (ln, line)
                    raise IOError(text)
                field = getfield(tag, itemtype)
                if field not in current:
                    current[field] = [getcontent(line)]
                else:
                    current[field].append(getcontent(line))
        else:
            if not line.strip():
                continue
            if inref:
                if tag is None:
                    text = "Expected tag in line %d:\n %s" % (ln, line)
                    raise IOError(text)
            else:
                if iscounter(line):
                    continue
                text = "Expected start tag in line %d:\n %s" % (ln, line)
                raise IOError(text)


'''LIST_TYPE_TAGS = [
    'A1',
    'A2',
    'A3',
    'A4',
    'AU',
    'KW',
]'''

KEYLENGTH = 8
randomkey = lambda: ''.join(random.choice(string.uppercase + string.digits) for i in range(KEYLENGTH))
safepath = lambda a: re.sub('[^\w\-_. ]', '_', a)

# mapping from zotero
DEFAULT_EXPORT_TYPE = 'GEN'
DEFAULT_IMPORT_TYPE = 'journalArticle'

fieldMap = {
    # same for all itemTypes
    "AB": "abstractNote",
    "AN": "archiveLocation",
    "CN": "callNumber",
    "DB": "archive",
    "DO": "DOI",
    "DP": "libraryCatalog",
    "J2": "journalAbbreviation",
    "KW": "tags",
    "L1": "attachments/PDF",
    "L2": "attachments/HTML",
    "L4": "attachments/other",
    "N1": "notes",
    "ST": "shortTitle",
    "UR": "url",
    "Y2": "accessDate",

    # type specific
    # tag => field:itemTypes
    # if itemType not explicitly given, __default field is used
    # unless itemType is excluded in __exclude
    "TI": {
        "__default": "title",
        "subject": ["email"],
        "caseName": ["case"],
        "nameOfAct": ["statute"]
    },
    "T1": {
        "__default": "title",
        "subject": ["email"],
        "caseName": ["case"],
        "nameOfAct": ["statute"]
    },
    "T2": {
        # most item types should be covered above
        "__default": "backupPublicationTitle",
        "code": ["bill", "statute"],
        "bookTitle": ["bookSection"],
        "blogTitle": ["blogPost"],
        "conferenceName": ["conferencePaper"],
        "dictionaryTitle": ["dictionaryEntry"],
        "encyclopediaTitle": ["encyclopediaArticle"],
        "committee": ["hearing"],
        "forumTitle": ["forumPost"],
        "websiteTitle": ["webpage"],
        "programTitle": ["radioBroadcast", "tvBroadcast"],
        "meetingName": ["presentation"],
        "seriesTitle": ["computerProgram", "map", "report"],
        "series": ["book"],
        "publicationTitle": ["journalArticle", "magazineArticle", "newspaperArticle"]
    },
    "T3": {
        "legislativeBody": ["hearing", "bill"],
        "series": ["bookSection", "conferencePaper", "journalArticle", "book"],
        "seriesTitle": ["audioRecording"]
    },
    # NOT HANDLED: reviewedAuthor, scriptwriter, contributor, guest
    "AU": {
        "__default": "creators/author",
        "creators/artist": ["artwork"],
        "creators/cartographer": ["map"],
        "creators/composer": ["audioRecording"],
        # this clashes with audioRecording
        "creators/director": ["film", "radioBroadcast", "tvBroadcast", "videoRecording"],
        "creators/interviewee": ["interview"],
        "creators/inventor": ["patent"],
        "creators/podcaster": ["podcast"],
        "creators/programmer": ["computerProgram"]
    },
    "A2": {
        "creators/sponsor": ["bill"],
        "creators/performer": ["audioRecording"],
        "creators/presenter": ["presentation"],
        "creators/interviewer": ["interview"],
        "creators/editor": ["journalArticle", "bookSection", "conferencePaper",
                            "dictionaryEntry", "document", "encyclopediaArticle"],
        "creators/seriesEditor": ["book", "report"],
        "creators/recipient": ["email", "instantMessage", "letter"],
        "reporter": ["case"],
        "issuingAuthority": ["patent"]
    },
    "A3": {
        "creators/cosponsor": ["bill"],
        "creators/producer": ["film", "tvBroadcast", "videoRecording", "radioBroadcast"],
        "creators/editor": ["book"],
        "creators/seriesEditor": ["bookSection", "conferencePaper", "dictionaryEntry", "encyclopediaArticle", "map"]
    },
    "A4": {
        "__default": "creators/translator",
        "creators/counsel": ["case"],
        "creators/contributor": ["conferencePaper", "film"]  # translator does not fit these
    },
    "C1": {
        "filingDate": ["patent"],  # not in spec
        "creators/castMember": ["radioBroadcast", "tvBroadcast", "videoRecording"],
        "scale": ["map"],
        "place": ["conferencePaper"]
    },
    "C2": {
        "issueDate": ["patent"],  # not in spec
        "creators/bookAuthor": ["bookSection"],
        "creators/commenter": ["blogPost"]
    },
    "C3": {
        "artworkSize": ["artwork"],
        "proceedingsTitle": ["conferencePaper"],
        "country": ["patent"]
    },
    "C4": {
        "creators/wordsBy": ["audioRecording"],  # not in spec
        "creators/attorneyAgent": ["patent"],
        "genre": ["film"]
    },
    "C5": {
        "references": ["patent"],
        "audioRecordingFormat": ["audioRecording", "radioBroadcast"],
        "videoRecordingFormat": ["film", "tvBroadcast", "videoRecording"]
    },
    "C6": {
        "legalStatus": ["patent"],
    },
    "CY": {
        "__default": "place",
        "__exclude": ["conferencePaper"]  # should be exported as C1
    },
    "DA": {  # also see PY when editing
        "__default": "date",
        "dateEnacted": ["statute"],
        "dateDecided": ["case"],
        "issueDate": ["patent"]
    },
    "ET": {
        "__default": "edition",
        #       "__ignore":["journalArticle"], #EPubDate
        "session": ["bill", "hearing", "statute"],
        "version": ["computerProgram"]
    },
    "IS": {
        "__default": "issue",
        "numberOfVolumes": ["bookSection"]
    },
    "LA": {
        "__default": "language",
        "programmingLanguage": ["computerProgram"]
    },
    "M1": {
        "seriesNumber": ["book"],
        "billNumber": ["bill"],
        "system": ["computerProgram"],
        "documentNumber": ["hearing"],
        "applicationNumber": ["patent"],
        "publicLawNumber": ["statute"],
        "episodeNumber": ["podcast", "radioBroadcast", "tvBroadcast"],
        "__default": "extra",
        "issue": ["journalArticle"],  # EndNote hack
        "numberOfVolumes": ["bookSection"],  # EndNote exports here instead of IS
        "accessDate": ["webpage"]  # this is access date when coming from EndNote
    },
    "M2": "extra",  # not in spec
    "M3": {
        "__default": "DOI",
        "manuscriptType": ["manuscript"],
        "mapType": ["map"],
        "reportType": ["report"],
        "thesisType": ["thesis"],
        "websiteType": ["blogPost", "webpage"],
        "postType": ["forumPost"],
        "letterType": ["letter"],
        "interviewMedium": ["interview"],
        "presentationType": ["presentation"],
        "artworkMedium": ["artwork"],
        "audioFileType": ["podcast"]
    },
    "NV": {
        "__default": "numberOfVolumes",
        "__exclude": ["bookSection"]  # IS
    },
    "OP": {
        "history": ["hearing", "statute", "bill", "case"],
        "priorityNumbers": ["patent"],
        "__default": "unsupported/Original Publication",
        "unsupported/Content": ["blogPost", "computerProgram", "film", "presentation", "report", "videoRecording",
                                "webpage"]
    },
    "PB": {
        "__default": "publisher",
        "label": ["audioRecording"],
        "court": ["case"],
        "distributor": ["film"],
        "assignee": ["patent"],
        "institution": ["report"],
        "university": ["thesis"],
        "company": ["computerProgram"],
        "studio": ["videoRecording"],
        "network": ["radioBroadcast", "tvBroadcast"]
    },
    "PY": {  # duplicate of DA, but this will only output year
        "__default": "date",
        "dateEnacted": ["statute"],
        "dateDecided": ["case"],
        "issueDate": ["patent"]
    },
    "SE": {
        "__default": "section",
        # though this can refer to pages, start page, etc. for some types.
        # Zotero does not support any of those combinations, however.
        #        "__exclude": ["case"]
        "unsupported/File Date": ["case"]
    },
    "SN": {
        "__default": "ISBN",
        "ISSN": ["journalArticle", "magazineArticle", "newspaperArticle"],
        "patentNumber": ["patent"],
        "reportNumber": ["report"],
    },
    "SP": {
        "__default": "pages",  # needs extra processing
        "codePages": ["bill"],  # bill
        "numPages": ["book", "thesis", "manuscript"],  # manuscript not really in spec
        "firstPage": ["case"],
        "runningTime": ["film"]
    },
    "SV": {
        "seriesNumber": ["bookSection"],
        "docketNumber": ["case"]  # not in spec. EndNote exports this way
    },
    "VL": {
        "__default": "volume",
        "codeNumber": ["statute"],
        "codeVolume": ["bill"],
        "reporterVolume": ["case"],
        #        "__exclude":["patent", "webpage"]
        "unsupported/Patent Version Number": ['patent'],
        "accessDate": ["webpage"]  # technically access year according to EndNote
    },
    # degenerateImportFieldMap = {
    "A1": {
        "__default": "creators/author",
        "creators/artist": ["artwork"],
        "creators/cartographer": ["map"],
        "creators/composer": ["audioRecording"],
        "creators/director": ["film", "radioBroadcast", "tvBroadcast", "videoRecording"],
        # this clashes with audioRecording
        "creators/interviewee": ["interview"],
        "creators/inventor": ["patent"],
        "creators/podcaster": ["podcast"],
        "creators/programmer": ["computerProgram"]
    },
    "AD": {
        "__default": "unsupported/Author Address",
        "unsupported/Inventor Address": ["patent"]
    },
    "AV": "archiveLocation",  # REFMAN
    "BT": {
        "title": ["book", "manuscript"],
        "bookTitle": ["bookSection"],
        "__default": "backupPublicationTitle"  # we do more filtering on this later
    },
    "CA": "unsupported/Caption",
    "CR": "rights",
    "CT": "title",
    "ED": "creators/editor",
    "EP": "pages",
    "H1": "unsupported/Library Catalog",  # Citavi specific (possibly multiple occurences)
    "H2": "unsupported/Call Number",  # Citavi specific (possibly multiple occurences)
    "ID": "__ignore",
    "JA": "journalAbbreviation",
    "JF": "publicationTitle",
    "JO": {
        "__default": "journalAbbreviation",
        "conferenceName": ["conferencePaper"]
    },
    "LB": "unsupported/Label",
    "N2": "abstractNote",
    "RI": {
        "__default": "unsupported/Reviewed Item",
        "unsupported/Article Number": ["statute"]
    },
    "RN": "notes",
    "TA": "unsupported/Translated Author",
    "TT": "unsupported/Translated Title",
    "Y1": {  # also see PY when editing
        "__default": "date",
        "dateEnacted": ["statute"],
        "dateDecided": ["case"],
        "issueDate": ["patent"]
    }
}


def getpersonname(tom):
    namelist = tom.split(',')
    if len(namelist) == 2:
        lastname, firstname = namelist
    elif len(namelist) == 1:
        lastname = namelist[0]
        firstname = None
    else:
        msg = 'Bad defined name ' + tom
        return False, msg
    return True, (lastname, firstname)


def getfield(tag, itemtype=None):
    value = fieldMap[tag]
    try:
        field = value['__default']
    except:
        field = None
    if type(value) == dict:
        # search itemtype
        typeview = value.viewvalues()
        fieldview = value.viewkeys()
        # attribute default value for field
        if (not itemtype) and (not field):
            msg = 'Neither field nor default value is found!'
            raise IOError(msg)
        else:
            if ('__exclude' in fieldview) and (itemtype == value['__exclude']):
                msg = 'This type-field relation is excluded!'
                raise IOError(msg)
            else:
                for idx, typelist in enumerate(typeview):
                    if itemtype in typelist:
                        field = list(fieldview)[idx]
                        break
    else:
        field = value
    if field:
        return field
    else:
        msg = 'No field type is found!'
        raise IOError(msg)


def getfieldtype(entry):
    # whether field or creator
    sf = entry.split('/')
    if len(sf) == 1:
        fieldtype = 'field'
        field = sf[0]
    elif len(sf) == 2:
        fieldtype = sf[0]
        field = sf[1]
    else:
        msg = 'Unknown Field Type!'
        return False, msg
    return True, (fieldtype, field)


# RISparser is modified from https:#github.com/MrTango/RISparser

# Parse WOK and Refman's RIS files


def importris(risfile):
    with open(risfile, 'r') as bibliography_file:
        entries = readris(bibliography_file)
    return list(entries)


if __name__ == "__main__":
    ris_list = importris(ris_path)
    print("done")
