BP_vraagstelling_standaard = [
    '''Heeft u een ziekte of gebrek kunnen vaststellen op uw vakgebied? Zo ja, kunt u beschrijven welke symptomatologie op de voorgrond staat en wat de belangrijkste beïnvloedende factoren zijn?''',
    '''Wat is de classificatie volgens de DSM-5-TR?''',
    '''Wat zijn uw overwegingen ten aanzien van de validiteit van de anamnese?''',
    '''Zijn er beperkingen in het psychisch functioneren als gevolg van ziekte of gebrek? 
    - Zo ja, kunt u deze beschrijven? 
    - Kunt u een onderscheid maken tussen beperkingen die u geobserveerd heeft en beperkingen die u niet geobserveerd heeft?''',
    '''Heeft u aanvullende adviezen over de behandeling?''',
    '''Kunt u de volgende zaken met betrekking tot de prognose bespreken: 
    - Is er sprake van een chronische aandoening? 
    - Is er sprake van gebleken therapieresistentie? 
    - Zijn er andere relevante zaken die invloed hebben op de prognose?''',
    '''Heeft u gebruik gemaakt van externe informatie? 
    - Zo ja, zijn uw conclusies congruent met deze informatie? 
    - Kunt een verklaring geven voor eventuele discrepanties?'''
]


basis_rapport = {
    "bestandsnaam": "basis_rapport.docx",
    "voorblad": "yes",
    "inhoudsopgave": "yes",
    "titel": "Rapportage",
    "subtitel": "Subtitel",
    "hoofdstukken": [
        {
            "naam": "Algemeen",
            "paragrafen": [
                {"naam": "Context", "inhoud": "paragraaf_inhoud"},
                {"naam": "Deskundige", "inhoud": "paragraaf_inhoud"},
                {"naam": "Onderzoeksactiviteiten", "inhoud": "paragraaf_inhoud"},
                {"naam": "Identificatie", "inhoud": "paragraaf_inhoud"},
                {"naam": "Meegezonden informatie", "inhoud": "paragraaf_inhoud"},
                {"naam": "Correcties", "inhoud": "paragraaf_inhoud"},
                {"naam": "Inzage- en blokkering", "inhoud": "paragraaf_inhoud"},
                {"naam": "Commentaar", "inhoud": "paragraaf_inhoud"},
                {"naam": "Vraagstelling", "inhoud": "paragraaf_inhoud"},
            ],
        },
        {
            "naam": "Onderzoek",
            "paragrafen": [{"naam": "paragraaf_naam", "inhoud": "paragraaf_inhoud"}],
        },
        {
            "naam": "Bespreking",
            "paragrafen": [
                {"naam": "Samenvatting", "inhoud": "paragraaf_inhoud"},
                {"naam": "Beschouwing", "inhoud": "paragraaf_inhoud"},
            ],
        },
        {"naam": "Beantwoording vraagstelling", "paragrafen": []},
    ],
}


basis_rapport_v2 = {
    "bestandsnaam": "basis_rapport.docx",
    "voorblad": "yes",
    "inhoudsopgave": "yes",
    "titel": "Rapportage",
    "subtitel": "Subtitel",
    "hoofdstukken": {
        "Algemeen": {
            "Context": {},
            "Deskundige": {},
            "Onderzoeksactiviteiten" : {},
            "Identificatie": {
                "tekst": "De identiteit van betrokkene werd gecontroleerd"
            },
            "Meegezonden informatie": {},
            "Correcties": {
                "subparagrafen": []
            },
            "Inzage- en blokkering": {},
            "Commentaar": {},
            "Vraagstelling": {
                "vragen": BP_vraagstelling_standaard
            }
        },
        "Onderzoek":{
            "Anamnese": {},
            "Psychiatrisch onderzoek":{
                "subparagrafen" : {"Eerste indrukken":"",
                                   "Congnitieve functies":"",
                                   "Affectieve functies": "",
                                   "Conatieve functies": "",
                                   "Persoonlijkheidstrekken": "Persoonlijkheidstrekken volgens DSM5"}
            }
        },
        "Bespreking":{},
        "Beantwoording vraagstelling":{
            "Vraagstelling": { 
                "vragen": BP_vraagstelling_standaard
            }
        },        
    },
}
