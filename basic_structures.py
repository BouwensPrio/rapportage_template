from pprint import pprint
import copy


vraagstelling_standaard = [
    """Heeft u een ziekte of gebrek kunnen vaststellen op uw vakgebied? Zo ja, kunt u beschrijven welke symptomatologie op de voorgrond staat en wat de belangrijkste beïnvloedende factoren zijn?""",
    """Wat is de classificatie volgens de DSM-5-TR?""",
    """Wat zijn uw overwegingen ten aanzien van de validiteit van de anamnese?""",
    """Zijn er beperkingen in het psychisch functioneren als gevolg van ziekte of gebrek? \n- Zo ja, kunt u deze beschrijven? \n- Kunt u een onderscheid maken tussen beperkingen die u geobserveerd heeft en beperkingen die u niet geobserveerd heeft?""",
    """Heeft u aanvullende adviezen over de behandeling?""",
    """Kunt u de volgende zaken met betrekking tot de prognose bespreken: \n- Is er sprake van een chronische aandoening? \n- Is er sprake van gebleken therapieresistentie? \n- Zijn er andere relevante zaken die invloed hebben op de prognose?""",
    """Heeft u gebruik gemaakt van externe informatie? \n- Zo ja, zijn uw conclusies congruent met deze informatie? \n- Kunt een verklaring geven voor eventuele discrepanties?""",
]

vraagstelling_icara = [
    """Kunt u een diagnose stellen op uw vakgebied?""",
    """Zijn de ervaren klachten medisch objectiveerbaar?""",
    """Is de huidige behandeling adequaat?""",
    """Heeft u aanvullende behandeladviezen?""",
    """Kunt u een prognose geven?""",
]

correcties_algemeen = "Betrokkene wordt in de gelegenheid gesteld om feitelijke onjuistheden te corrigeren.\nHet concept rapport werd daartoe op [DATUM] aan betrokkene toegestuurd met het verzoek vóór [DATUM_2] te reageren.\nDe termijn werd op verzoek van betrokkene éénmalig verlengd tot [DATUM_3]\nBetrokkene reageerde niet voor het verlopen van de de termijn, ik ben er daarom van uit gegaan dat er geen feitelijke onjuistheden waren.\nBetrokkene reageerde voor het verlopen van de termijn. Ik heb de reactie bekeken en waar aangewezen correcties uitgevoerd."

geen_inzage_blokkering = "Gezien de juridische context waarbinnen het rapport is uitgebracht, is het inzage- en blokkeringsrecht niet van toepassing.\nHet rapport is na ontvangst en waar van toepassing, verwerking van correcties, dan wel na aflopen van de termijn voor het aanbrengen van correcties, op [DATUM] in definitieve vorm verzonden aan betrokkene en aan opdrachtgever"

commentaar_algemeen = "Na verzending van het definitieve rapport zijn zowel opdrachtgever als betrokkene in de gelegenheid gesteld om commentaren en eventuele aanvullende vragen aan te leveren. Aanvullende vragen worden uitsluitend in behandeling genomen waar die duidelijk vragen om verheldering van de werkwijze of de onderbouwing. De termijn voor het aanleveren van commentaar verloopt op [DATUM]. De deskundige reageert daarna éénmaal op de commentaren van zowel opdrachtgever als betrokkene. Na deze reactie wordt het onderzoek definitief afgerond."

context_algemene_toelichting = "Controleer altijd of de context juist is (arbeidsrechtelijk, civielrechtelijk, bestuursrechtelijk,...) en verbeter deze waar nodig. Ook kan hier een korte schets van de toedracht tot het onderzoek gegeven worden."

contexten = {
    "AOV": {
        "Context": {
            "toelichting": context_algemene_toelichting,
            "tekst": "De rapportage wordt in een civielrechtelijk kader uitgevoerd op verzoek van de particuliere arbeidsongeschiktheidsverzekeraar van betrokkene",
        },
        "Correcties": correcties_algemeen,
        "Inzage- en blokkering": geen_inzage_blokkering,
        "Commentaar": commentaar_algemeen,
    },
    "Arbeidsrecht": {
        "Context": {
            "toelichting": context_algemene_toelichting,
            "tekst": "De rapportage wordt in een arbeidsrechtelijk kader uitgevoerd in opdracht van de werkgever c.q. de bedrijfsarts van betrokkene ten behoeve van de uitvoering van de WVP",
        },
        "Correcties": correcties_algemeen,
        "Inzage- en blokkering": geen_inzage_blokkering,
        "Commentaar": commentaar_algemeen,
    },
    "IGJ": {
        "Context": "De rapportage wordt uitgevoerd in opdracht van de inspectie gezondheidszorg en jeugd",
        "Correcties": correcties_algemeen,
        "Inzage- en blokkering": "Het inzage- en blokkeringsrecht zijn van toepassing. Betrokkene heeft op [DATUM] ter inzage het definitieve rapport toegestuurd gekregen. Aan betrokkene werd daarbij verzocht om voor [DATUM_2] kenbaar te maken of hij/zij akkoord gaat met verzending van de rapportage.\nBetrokkene reageerde op [DATUM_3] op dit verzoek en gaf daarbij aan dat het rapport WEL/NIET geblokkeerd was. Het rapport is daartoe [NIET VERZONDEN/VERZONDEN AAN DE OPDRACHTGEVER OP DATUM_4]\nBetrokkene reageerde niet binnen de daartoe afgesproken termijn, het rapport wordt daarom als geblokkeerd beschouwd en opdrachtgever werd daarvan op [DATUM_4] op de hoogte gesteld.",
        "Commentaar": commentaar_algemeen,
    },
    "Bestuursrecht": {
        "Context": {
            "toelichting": "In verband met eventueel recht op een uitkering krachtens de Ziektewet, de WAO/WIA/WGA/IVA of de Wajong moet vaststaan dat er sprake is van ziekte of gebrek. Volgens jurisprudentie van de Centrale Raad van Beroep moet de beoordelend arts ervan overtuigd zijn dat er sprake is van ziekte. Het is daarvoor niet altijd noodzakelijk dat ook een eenduidige diagnose kan worden gesteld. Wel moet de deskundige onderbouwen dat hij het klachtverhaal voldoende plausibel en consistent acht. Bij dit onderzoek is in de regel sprake van een datum in geding. Dat betekent dat uit het rapport moet blijken dat de deskundige zijn onderzoek en zijn uitspraken heeW gebaseerd op de situaIe zoals deze was op de betreffende (peil)datum.",
            "tekst": "De rapportage wordt in een bestuursgerechtelijk kader uitgevoerd in opdracht van [RECHTBANK/CRvB] inzake een (hoger) beroep van betrokkene tegen een beslissing van het UWV omtrent de mate van arbeidsongeschiktheid en/of het aanspraak maken op een uitkering",
        },
        "Correcties": correcties_algemeen,
        "Inzage- en blokkering": "Inzage- en blokkeringsrecht zijn niet van toepassing. Na het eventueel verwerken van gewenste correcties, wordt het definitieve rapport rechtstreeks aan de [RECHTBANK/CRvB] verstuurd",
        "Commentaar": "Gezien de context waarbinnen het onderzoek plaatsvindt, is er geen commentaarfase. Partijen kunnen hun zienswijzen ter zitting aanhangig maken. Eventueel kan de [RECHTBANK/CRvB] aan deskundige aanvullende vragen voorleggen",
    },
}

basis_rapport = {
    "bestandsnaam": "basis_rapport.docx",
    "voorblad": "yes",
    "inhoudsopgave": "yes",
    "titel": "Rapportage",
    "subtitel": "Subtitel",
    "hoofdstukken": {
        "Algemeen": {
            "Context": {},
            "Deskundige": {
                "toelichting": "De deskundige is niet de behandelend arts van de betrokkene of bij diens behandeling betrokken. Het kan zijn dat blijkt dat de deskundige de betrokkene in het verleden heeW behandeld. Als deze behandeling al eerder werd afgesloten en er geen relaIe bestaat tot de voorliggende casus dient de deskundige zowel met de betrokkene als met de opdrachtgever(s) in overleg te treden of dit de rapportage in de weg zou staan. Pas als alle betrokkenen, dus ook de deskundige zelf, verklaren hierin geen bezwaar te zien, kan de deskundige het onderzoek verrichten. Echter, hierbij geldt het advies om bij twijfel de opdracht niet te aanvaarden en van rapportage af te zien. De deskundige aanvaardt ook geen opdracht als hij tevoren in dezelfde casus voor een van de parIjen als consulent is opgetreden of indien een van de partijen hem tevoren heeft gevraagd hoe hij in deze casus zou oordelen. (Richtlijn NVMSR art 4.4)",
                "tekst": "Voorafgaand aan het onderzoek heb ik vastgesteld dat ik betrokkene niet eerder heb behandeld, noch anderszins bij de behandeling betrokken ben geweest. Ook heb ik vastgesteld dat ik geen andere strijdige belangen heb die interfereren met een onafhankelijke beoordeling.",
            },
            "Onderzoeksactiviteiten": {
                "toelichting": "Op geen enkele wijze neemt de deskundige de rol van hulpverlener aan of suggereert hij die rol in de toekomst te gaan vervullen. Vanzelfsprekend dient de deskundige in een dringende situaIe conform de WGBO, als goed hulpverlener, te handelen en kan acute zorg worden verleend of contact worden opgenomen met de huisarts of behandelend arts. (Richtlijn NVMSR art 4.5)\a Bij de bejegening van de betrokkene worden de gebruikelijke, maatschappelijk aanvaarde omgangsvormen gehanteerd. De bejegening is vriendelijk en beleefd, maar tegelijk ook zakelijk en wordt gekenmerkt door professionele distanIe. Dat het contact vaak zakelijker is dan een contact in een curatief kader wordt bij voorkeur vooraf aan betrokkene kenbaar gemaakt. De deskundige verduidelijkt daarbij aan de betrokkene diens posiIe van ona]ankelijk deskundige. Om onterechte verwachIngen te voorkomen legt de deskundige uit dat er tussen hem en de betrokkene geen therapeuIsche of hulpverleningsrelatie kan bestaan.",
                "tekst": """Ik heb betrokkene onderzocht op:\a[DATUM] te [PLAATS] gedurende ... minuten. Het onderzoek vond face-to-face / online] plaats\a[DATUM] te [PLAATS] gedurende ... minuten. Het onderzoek vond face-to-face / online] plaats\a[DATUM] te [PLAATS] gedurende ... minuten. Het onderzoek vond face-to-face / online] plaats\aVoorafgaand aan het onderzoek heb ik betrokkene ingelicht over mijn onafhankelijke rol. In het bijzonder heb ik toegelicht dat er geen behandelrelatie tot stand komt. Tevens heb ik betrokkene ingelicht over de gang van zaken rondom het correctierecht, het inzage- en blokkeringsrecht en de commentaarfase. """,
            },
            "Identificatie": {
                "tekst": "De identiteit van betrokkene werd gecontroleerd voorafgaand aan het onderzoek\aDocumenttype: paspoort/identiteitsbewijs/rijbewijs/\aBSN:"
            },
            "Meegezonden informatie": {
                "tekst": "Voor een overzicht van de toegezonden stukken en de aanvullend opgevraagde stukken verwijs ik naar de betreffende bijlage"
            },
            "Correcties": {},
            "Inzage- en blokkering": {},
            "Commentaar": {},
            "Vraagstelling": {},
        },
        "Onderzoek": {},
        "Bespreking": {},
        "Beantwoording vraagstelling": {},
    },
}

basis_externe_info = {
    "bestandsnaam": "basis_externe_info.docx",
    "voorblad": "yes",
    "inhoudsopgave": "no",
    "titel": "Externe informatie",
    "subtitel": "",
    "hoofdstukken": {
        "Aangeleverde informatie": {
            "Overzicht van de stukken": {
                "toelichting": "Som hier de door de opdrachtgever en/of betrokkene aangeleverde stukken op zodat een overzicht ontstaat van de stukken. Houd daarbij telkens hetzelfde 'format' aan. bijvoorbeeld 'datum - soort - instantie - afzender' = '19-2-2019 - ontslagbrief - GGZ Rivierduinen - dhr. Z. Ielenknijper, psychiater"
            },
            "Relevante informatie": {
                "toelichting": "Geef hier per stuk aan wat relevant is. Doet dit zoveel mogelijk verbatim (kopiëren en plakken uit het brondocument) - het is hier niet de bedoeling dat er al een interpretatie wordt gegeven. Een conclusie uit een brief of een psychiatrisch onderzoek zou bijvoorbeeld 1-op-1 kunnen worden overgenomen."
            },
        },
        "Aanvullend opgevraagde informatie": {
            "Overzicht van de stukken": {
                "toelichting": "Som hier de door de aanvullend stukken op zodat een overzicht ontstaat van de stukken. Houd daarbij telkens hetzelfde 'format' aan. bijvoorbeeld 'datum - soort - instantie - afzender' = '19-2-2019 - ontslagbrief - GGZ Rivierduinen - dhr. Z. Ielenknijper, psychiater"
            },
            "Relevante informatie": {
                "toelichting": "Geef hier per stuk aan wat relevant is. Doet dit zoveel mogelijk verbatim (kopiëren en plakken uit het brondocument) - het is hier niet de bedoeling dat er al een interpretatie wordt gegeven. Een conclusie uit een brief of een psychiatrisch onderzoek zou bijvoorbeeld 1-op-1 kunnen worden overgenomen."
            },
        },
    },
}


basis_rapport_psychiatrie = {
    "bestandsnaam": "basis_rapport_psychiatrie.docx",
    "hoofdstukken": {
        "Onderzoek": {
            "Speciële anamnese": {},
            "Tractus anamnese": {
                "Bewustzijn": "",
                "Aandacht en concentratie": "",
                "Geheugen": "",
                "Metacognitie": "",
                "Waarneming": "",
                "Zelfwaarneming": "",
                "Denken": "",
                "Stemming": "",
                "Angsten": "",
                "Vitale kenmerken": "",
                "Trauma": "",
                "Life events": "",
                "Suïcidaliteit": "",
                "Psychomotoriek": "",
                "Impulsbeheersing": "",
                "Persoonlijkheid": "",
            },
            "Middelengebruik": {"Drugs": "", "Alcohol": "", "Roken": ""},
            "Sociale anamnese": {
                "Thuissituatie en eigen gezin": "",
                "Contacten met familieleden buiten het gezin": "",
                "Contacten met vrienden en kennissen": "",
                "Opleiding en werk": "",
                "Vrije tijd": "",
            },
            "Dagverhaal": {"verbergen": "ja"},
            "Persoonlijkheidsfunctioneren" : {"verbergen":"ja"},
            "Ontwikkelingsanamnese": {"verbergen": "ja"},
            "Biografie": {},
            "Heteroanamnese": {},
            "Familieanamnese": {},
            "Psychiatrische voorgeschiedenis": {},
            "Medicatie": {},
            "Somatische anamnese": {},
            "Somatische voorgeschiedenis": {},
            "Psychiatrisch onderzoek": {
                "Eerste indrukken": "",
                "Cognitieve functies": "",
                "Affectieve functies": "",
                "Conatieve functies": "",
                "Persoonlijkheidstrekken": {
                    "tekst": """Ten aanzien van persoonlijkheidstrekken wordt volstaan met een beschrijving van zich gedurende het onderzoek tonende persoonlijkheidstrekken conform de beoordelingslijst voor persoonlijkheidstrekken binnen de dimensionale classificatie van persoonlijkheidsstoornissen van de DSM-5-TR. Beschreven persoonlijkheidstrekken zijn niet zondermeer een uiting van een onderliggende stoornis in de persoonlijkheid maar kunnen ook een variatie van normaal zijn, situationeel bepaald of voortkomen uit een onderliggende psychische aandoening niet zijnde een persoonlijkheidsstoornis. \n\nBinnen het domein negatieve affectiviteit lijkt er sprake te zijn van emotionele labiliteit / ongerustheid / separatieangst / submissiviteit / vijandigheid / perseveratie / depressiviteit / achterdocht / ingeperkte affectiviteit \nBinnen het domein afstandelijkheid lijkt er sprake te zijn van sociale teruggetrokkenheid / vermijding van intimiteit / anhedonie / depressiviteit / ingeperkte affectiviteit / achterdocht \nBinnen het domein antagonisme lijkt er sprake te zijn van manipulatief gedrag / leugenachtigheid / grandiositeit / aandacht zoeken / ongevoeligheid / vijandigheid \nBinnen het domein ongeremdheid/dwangmatigheid lijkt er sprake te zijn van onverantwoordelijk gedrag / impulsiviteit / afleidbaarheid / riskant gedrag / rigide perfectionisme \nBinnen het domein psychoticisme lijkt er sprake te zijn van ongewone overtuigingen en ervaringen / excentriciteit / cognitieve en perceptuele disregulatie"""
                },
            },
        },
        "Bespreking": {},
    },
}

psychiatrie_belastbaarheid = {
    "bestandsnaam": "basis_belastbaarheid.docx",
    "hoofdstukken": {
        "Onderzoek": {
            "Speciële anamnese": {
                "toelichting": "Het rapport moet, ongeacht de opbouw, in ieder geval voldoen aan de volgende kwaliteitscriteria:\n1. In het rapport wordt op inzichtelijke en consistente wijze uiteengezet op welke gronden de conclusiesvan het rapport steunen.\n2. Bovenstaande gronden vinden aantoonbaar steun in de feiten, omstandigheden en bevindingen zoals die worden vermeld in het rapport.\n3. Het rapport geeW blijk van een binnen de beroepsgroep algemeen geaccepteerde methode van onderzoek om de voorgelegde vraagstelling te beantwoorden.\n4. Het rapport vermeldt de bronnen waarvan gebruik werd gemaakt, daarbij inbegrepen de gebruikte literatuur en de geconsulteerde personen.\n5. De rapporteur blijW binnen de grenzen van zijn deskundigheid. (Richtlijn NVMSR 2024 art 8.1)\a8.2 De beschrijving van de anamnese is deugdelijk en compleet en beperkt zich tot de relevante gegevens ten behoeve van de beantwoording van de aan de deskundige voorgelegde vragen. De beschrijving van de anamnese bevat uitsluitend het verhaal van de betrokkene, zoveel mogelijk in diens eigen bewoordingen. Er worden daarbij geen termen gebruikt of feiten vermeld die uitsluitend kunnen zijn ontleend aan aangeleverde of verkregen medische gegevens of een interpretaIe daarvan. Termen als “betrokkene zou (...)” worden vermeden. Ook voegt de deskundige bij de beschrijving van de anamnese geen voorlopige conclusies of eigen interpretaIes toe. De auto-anamnese en hetero-anamnese worden gescheiden weergegeven. (Richtlijn NVMSR 2024 art 8.2)",
                "Houding van betrokkene tegenover het onderzoek": "",
                "Toedracht van het onderzoek in de woorden van betrokkene": "",
                "Door betrokkene ervaren klachten": "",
                "Door betrokkene ervaren beperkingen in het functioneren": "",
            },
            "Dagverhaal": {},
            "Ontwikkelingsanamnese": {
                "Perinatale periode": "",
                "Motoriek en spraak": "",
                "Zindelijkheid": "",
                "Sociale ontwikkeling": "",
                "Intellectuele ontwikkeling": "",
            },
            "Bespreking": {
                "Samenvatting": {
                    "toelichting": "In de samenvatting worden alle relevante gegevens uit het voorgaande onderzoek kernachtig samengevat. Het betreft dus geen gedeeltelijke of volledige heraling van deze gegevens. Van belang is dat alleen de feiten uit het voorgaande worden weergegeven. De samenvatting bevat dus geen interpretaties, gevolgtrekkingen of hypotheses (uitgezonderd zijn de bevindingen uit het psychiatrisch onderzoek waarbij per definitie sprake is van interpretatie)."
                },
                "Beschouwing": {
                    "toelichting": "De beschouwing is de kern van het rapport. In de beschouwing komen alle overwegingen aan de rode die tot de beantwoording van de vraagstelling leiden.\aEen eventuele causaliteitsvraag wordt uitsluitend beantwoord vanuit de medische causaliteitsgedachte, dat wil zeggen op grond van datgene wat bekend en herkenbaar is met betrekking tot het ontstaan en het beloop van de onderhavige klachten en verschijnselen. Deze vaststelling gebeurt in overeenstemming met de gangbare wetenschappelijk inzichten dan wel richtlijnen binnen het desbetreffende vakgebied. De deskundige zal nooit anamnestische klachten en/of anamnestische beperkingen aan een gebeurtenis (bijvoorbeeld een ongeval of incident) toeschrijven of de causaliteit ervan louter baseren op grond van het feit dat deze na de gebeurtenis voor het eerst worden vermeld. De beoordeling van een eventueel juridisch causaal verband is voorbehouden aan parIjen en uiteindelijk de rechter. (Richtlijn NVMSR 2024 art 8.6)\aDe eventuele beperkingen van de betrokkene worden zo nauwkeurig mogelijk beschreven en slechts in semi-kwanItaIeve vorm weergegeven. De hierbij geadviseerde termen zijn ‘geen, licht, matig, ernstig, volledig’. De deskundige zal zelf geen kwantificerende belastbaarheidsprofielen opstellen. Alleen een bedrijfsarts of een verzekeringsarts is bekwaam om een FuncIonele Mogelijkhedenlijst (FML) op te stellen. De deskundige kan wel de vaststellingen in een FML becommentariëren vanuit het eigen vakgebied en op grond van de eigen waarnemingen.) (Richtlijn NVMSR 2024 art 8.7)\a De deskundige is eraan gehouden zich te beperken tot de beantwoording van de vraagstelling. Let dus goed op waar naar gevraagd wordt en beschouw en beantwoord alleen die zaken. Als er bijvoorbeeld niet naar een prognose en niet naar behandelmogelijkheden wordt gevraagd, dient dit ook niet beschouwd te worden. ",
                    "Consistentie en validiteit": "",
                    "Beschrijvende diagnose - context": "",
                    "Beschrijvende diagnose - door betrokkene ervaren en gerapporteerde klachten en beperkingen": "",
                    "Beschrijvende diagnose - door onderzoeker geobserveerde symptomen": "",
                    "Beschrijvende diagnose - hypothese over het persoonlijkheidsfunctioneren": "",
                    "Beschrijvende diagnose - hypothese over het toestandsbeeld": "",
                    "Beschrijvende diagnose - hypothese over beïnvloedende factoren": "",
                    "Classificerende diagnose": "",
                    "Differentiaal diagnose": "",
                    "Beperkingen in het functioneren": {
                        "toelichting": "Beschrijf hier op een feitelijke en objectiveerbare manier beperkingen in het psychisch functioneren als gevolg van de vastgestelde psychopathologie. Blijf hierbij binnen het eigen expertisegebied. Suggestie:\aCognitieve beperkingen\nIk heb tijdens mij onderzoek waargenomen dat ...\nBetrokkene heeft anamnestisch aangegeven beperkingen te ervaren op het gebied van ... \nUit het dagverhaal en [OVERIGE INFORMATIE] blijkt wel/niet dat betrokkene beperkt is op het gebied van ...\nIk vind het daarom geobjectiveerd dat betrokkene beperkt is op het gebied van [EIGEN WAARNEMINGEN] en ik vind het aannemelijk dat betrokkene beperkt is op het gebied van [HETGEEN BETROKKENE ZELF VERMELDT EN BLIJKT UIT DE COLLATERALE INFORMATIE]\aAffectieve beperkingen\aetc, etc..."
                    },
                    "Adviezen voor behandeling": {
                        "toelichting": "Wees hier voorzichtig. Een expertiseonderzoek is een hele andere context dan een intakegesprek binnen een indicatiestelling. Dat kun je ook gerust vermelden als de opdrachtgever een hele expliciete vraag over behandeling stelt. Beperk je in principe tot het wijzen op de betreffende richtlijn, tenzij er duidelijke argumenten zijn om dat niet te doen. Indien er een lopende behandeling is mogen we waar wel kritisch over zijn maar tegelijkertijd moeten we de huidige behandelaar (mits BIG registreerd) in het zadel laten zitten."
                    },
                    "Prognostische overwegingen": {
                        "toelichting": "Bespreek dit altijd systematisch. Begin met de meeste objectieve constateringen. Bespreek in ieder geval: \aDe aard van de aandoening, is deze chronisch/episodisch/progressief of van voorbijgaande aard? (Indien een DSM-classificatie goed past bij de beschrijvende diagnostiek kan ook het betreffende hoofdstuk omtrent prognose uit de DSM-5-TR geraadpleegd worden) \aOf er sprake is van gebleken therapieresistentie, daar is sprake van als er meerdere adequate behandelingen zijn uitgevoerd zonder resultaat. Adequaat betekend de juiste behandeling én de juiste uitvoering van de behandeling. Dat is in principe de behandeling volgens de richtlijn maar beargumenteerd kan daar natuurlijk van worden afgeweken. \aBespreek vervolgens andere bekende prognostische factoren: comorbiditeit, sociaal-maatschappelijke problematiek, middelenmisbruik etc. \aHet is voor de conclusie op dit punt het belangrijkst om aan te geven óf er nog significant herstel te verwachten is binnen welke termijn dit redelijkerwijs te verwachten is (denk in termijnen van halve jaren, niet maanden of weken) en of er terugval te verwachten is (zoals bij bipolariteit, verslaving)"
                    },
                    "Weging van de externe stukken": {
                        "toelichting": "Vat hier niet opnieuw de stukken samen en beschouw deze ook niet maar bespreek of de eigen bevindingen in lijn zijn met de bevindingen van eerdere GGZ-professionals. Maak het in ieder geval kenbaar als er grote afwijkingen zijn en probeer een verklaring te bieden. Als een verklaring niet geboden kan worden, bijvoorbeeld om dat de eigen behandelaar alleen een DSM-classificatie heeft gegeven en geen onderbouwing, zeg dat dan - het belangrijkste van deze paragraaf is het kenbaar maken van het gezien hebben van verschillen en het expliciet tonen van de bereidheid om daarover na te denken."
                    },
                },
                "DSM-5-TR": {},
                "Conclusie": {
                    "toelichting": "De beantwoording van de vraagstelling volgt op logische wijze uit de conclusie. De gevolgtrekkingen uit de beschouwing zijn de bron van de conclusie. De conclusie vermeldt dus de gevolgtrekkingen die relevant zijn voor de beantwoording van de vraagstelling. De conclusie bevat geen (herhaling van de) samenvatting of uitgebreide voorbeelden en nuanceringen tenzij dit echt strikt noodzakelijk is voor een juist interpretatie van de gevolgtrekking. Evenmin bevat de conclusie gevolgtrekkingen die niet terug te vinden en onderbouwd zijn in de beschouwing."
                },
            },
        },
    },
}

arbeidsrecht_belastbaarheid = {
    "bestandsnaam": "BP_belastbaarheid_arbeidsrecht.docx",
    "titel": "Arbeidsrechtelijke rapportage",
    "subtitel": "",
    "hoofdstukken": {
        "Algemeen": {
            "Context": contexten["Arbeidsrecht"]["Context"],
            "Correcties": {"tekst": contexten["Arbeidsrecht"]["Correcties"]},
            "Inzage- en blokkering": {
                "tekst": contexten["Arbeidsrecht"]["Inzage- en blokkering"]
            },
            "Commentaar": {"tekst": contexten["Arbeidsrecht"]["Commentaar"]},
            "Vraagstelling": {
                "toelichting": "Controleer altijd of de vraagstelling juist is en of er nog aanvullende of afwijkende vragen zijn, vul aan/pas aan/verwijder waar nodig",
                "vragen": vraagstelling_standaard,
            },
        },
        "Beantwoording vraagstelling": {
            "Vraagstelling": {
                "toelichting": "De vragen worden volledig, begrijpelijk en vooral eenduidig beantwoord. Bij de beantwoording van de vragen komen niet/nooit plotseling aspecten naar voren, die niet worden ondersteund/onderbouwd in de voorafgaande beschouwing.",
                "vragen": vraagstelling_standaard,
            }
        },
    },
}

bestuurssrecht_belastbaarheid = {
    "bestandsnaam": "BP_bestuursrecht.docx",
    "titel": "Bestuursrechtelijke rapportage",
    "subtitel": "Onafhankelijke psychiatrische expertise",
    "hoofdstukken": {
        "Algemeen": {
            "Context": contexten["Bestuursrecht"]["Context"],
            "Correcties": {"tekst": contexten["Bestuursrecht"]["Correcties"]},
            "Inzage- en blokkering": {
                "tekst": contexten["Bestuursrecht"]["Inzage- en blokkering"]
            },
            "Commentaar": {"tekst": contexten["Bestuursrecht"]["Commentaar"]},
            "Vraagstelling": {
                "toelichting": "Controleer altijd of de vraagstelling juist is en of er nog aanvullende of afwijkende vragen zijn, vul aan/pas aan/verwijder waar nodig"
            },
        },
        "Bespreking": {
            "Samenvatting": {
                "toelichting": "In de samenvatting worden alle relevante gegevens uit het voorgaande onderzoek kernachtig samengevat. Het betreft dus geen gedeeltelijke of volledige heraling van deze gegevens. Van belang is dat alleen de feiten uit het voorgaande worden weergegeven. De samenvatting bevat dus geen interpretaties, gevolgtrekkingen of hypotheses (uitgezonderd zijn de bevindingen uit het psychiatrisch onderzoek waarbij per definitie sprake is van interpretatie).",
                "Anamnese": "",
                "Psychiatrisch onderzoek": "",
                "Meetinstrumenten": "",
                "Externe stukken": "",
            },
            "Beschouwing": {
                "toelichting": "De beschouwing is de kern van het rapport. In de beschouwing komen alle overwegingen aan de rode die tot de beantwoording van de vraagstelling leiden.\aEen eventuele causaliteitsvraag wordt uitsluitend beantwoord vanuit de medische causaliteitsgedachte, dat wil zeggen op grond van datgene wat bekend en herkenbaar is met betrekking tot het ontstaan en het beloop van de onderhavige klachten en verschijnselen. Deze vaststelling gebeurt in overeenstemming met de gangbare wetenschappelijk inzichten dan wel richtlijnen binnen het desbetreffende vakgebied. De deskundige zal nooit anamnestische klachten en/of anamnesIsche beperkingen aan een gebeurtenis (bijvoorbeeld een ongeval of incident) toeschrijven of de causaliteit ervan louter baseren op grond van het feit dat deze na de gebeurtenis voor het eerst worden vermeld. De beoordeling van een eventueel juridisch causaal verband is voorbehouden aan parIjen en uiteindelijk de rechter. (Richtlijn NVMSR 2024 art 8.6)\aDe eventuele beperkingen van de betrokkene worden zo nauwkeurig mogelijk beschreven en slechts in semi-kwanItaIeve vorm weergegeven. De hierbij geadviseerde termen zijn ‘geen, licht, matig, ernstig, volledig’. De deskundige zal zelf geen kwantificerende belastbaarheidsprofielen opstellen. Alleen een bedrijfsarts of een verzekeringsarts is bekwaam om een FuncIonele Mogelijkhedenlijst (FML) op te stellen. De deskundige kan wel de vaststellingen in een FML becommentariëren vanuit het eigen vakgebied en op grond van de eigen waarnemingen.) (Richtlijn NVMSR 2024 art 8.7)\aVolgens jurisprudentie van de Centrale Raad van Beroep moet de beoordelend arts ervan overtuigd zijn dat er sprake is van ziekte. Het is daarvoor niet altijd noodzakelijk dat ook een eenduidige diagnose kan worden gesteld. Wel moet de deskundige onderbouwen dat hij het klachtverhaal voldoende plausibel en consistent acht. Bij dit onderzoek is in de regel sprake van een datum in geding. Dat betekent dat uit het rapport moet blijken dat de deskundige zijn onderzoek en zijn uitspraken heeW gebaseerd op de situaIe zoals deze was op de betreffende (peil)datum (Richtlijn NVMSR 2024 - specifieke aspecten bij rapportages in het bestuursrecht)\aDe deskundige is eraan gehouden zich te beperken tot de beantwoording van de vraagstelling. Let dus goed op waar naar gevraagd wordt en beschouw en beantwoord alleen die zaken. Als er bijvoorbeeld niet naar een prognose en niet naar behandelmogelijkheden wordt gevraagd, dient dit ook niet beschouwd te worden.",
                "Validiteit van de anamnese": "",
                "Beschrijvende diagnose": "",
                "Classificerende diagnose": "",
                "Differentiaal diagnostische overwegingen": "",
                "Diagnostiek op de in geding zijnde datum": "",
                "Beperkingen in het functioneren op de in geding zijnde datum": "",
                "Weging van de externe stukken": "",
            },
        },
        "Beantwoording vraagstelling": {
            "Vraagstelling": {
                "toelichting": "De vragen worden volledig, begrijpelijk en vooral eenduidig beantwoord. Bij de beantwoording van de vragen komen niet/nooit plotseling aspecten naar voren, die niet worden ondersteund/onderbouwd in de voorafgaande beschouwing.",
                "vragen": "",
            }
        },
    },
}

icara_belastbaarheid = {
    "bestandsnaam": "BP_belastbaarheid_compact.docx",
    "titel": "Psychiatrische rapportage",
    "subtitel": "",
    "hoofdstukken": {
        "Algemeen": {
            "Context": {
                "tekst": "Het onderzoek vindt plaats in opdracht van de verzekeringsarts van Icara teneinde bij te dragen aan een onafhankelijke beoordeling van de medische belastbaarheid van betrokkene."
            },
            "Correcties": {
                "tekst": "Betrokkene krijgt de gelegenheid om feitelijke correcties aan te brengen."
            },
            "Inzage- en blokkering": {
                "tekst": "Inzage- en blokkeringsrecht zijn niet van toepassing"
            },
            "Commentaar": {
                "tekst": "Betrokkene heeft de gelegenheid om commentaren en vragen over het rapport aan te leveren"
            },
            "Vraagstelling": {
                "toelichting": "Controleer altijd of de vraagstelling juist is en of er nog aanvullende of afwijkende vragen zijn, vul aan/pas aan/verwijder waar nodig",
                "vragen": vraagstelling_icara,
            },
        },
        "Onderzoek": {
            "Speciële anamnese": {
                "Toedracht van het onderzoek": "",
                "Houding tegenover het onderzoek": "",
                "Door betrokkene ervaren klachten": "",
                "Door betrokkene ervaren beperkingen in het functioneren": "",
            },
            "Ontwikkelingsanamnese": {},
            "Sociale anamnese": {},
        },
        "Bespreking": {
            "Beschouwing": {
                "Validiteit van de anamnese": "",
                "Beschrijvende diagnose": "",
                "Classificerende diagnose": "",
                "Differentiaal diagnostische overwegingen": "",
                "Adviezen voor behandeling": "",
                "Prognose": "",
                "Weging van de externe stukken": "",
            },
        },
        "Beantwoording vraagstelling": {
            "Vraagstelling": {"vragen": vraagstelling_icara}
        },
    },
}

AOV_belastbaarheid = {
    "bestandsnaam": "BP_AOV_belastbaarheid.docx",
    "titel": "Psychiatrische rapportage AOV",
    "hoofdstukken": {
        "Algemeen": {
            "Context": contexten["AOV"]["Context"],
            "Correcties": {"tekst": contexten["AOV"]["Correcties"]},
            "Inzage- en blokkering": {
                "tekst": contexten["AOV"]["Inzage- en blokkering"]
            },
            "Commentaar": {"tekst": contexten["AOV"]["Commentaar"]},
            "Vraagstelling": {
                "toelichting": "Controleer altijd of de vraagstelling juist is en of er nog aanvullende of afwijkende vragen zijn, vul aan/pas aan/verwijder waar nodig"
            },
        },
        "Beantwoording vraagstelling": {
            "Vraagstelling": {
                "toelichting": "De vragen worden volledig, begrijpelijk en vooral eenduidig beantwoord. Bij de beantwoording van de vragen komen niet/nooit plotseling aspecten naar voren, die niet worden ondersteund/onderbouwd in de voorafgaande beschouwing.",
                "vragen": "",
            }
        },
    },
}

IGJ_belastbaarheid = {
    "bestandsnaam": "BP_IGJ_expertise.docx",
    "titel": "Psychiatrische rapportage IGJ",
    "hoofdstukken": {
        "Algemeen": {
            "Context": {"tekst": contexten["IGJ"]["Context"]},
            "Correcties": {"tekst": contexten["IGJ"]["Correcties"]},
            "Inzage- en blokkering": {
                "tekst": contexten["IGJ"]["Inzage- en blokkering"]
            },
            "Commentaar": {"tekst": contexten["IGJ"]["Commentaar"]},
        },
        "Beantwoording vraagstelling": {
            "Vraagstelling": {
                "toelichting": "De vragen worden volledig, begrijpelijk en vooral eenduidig beantwoord. Bij de beantwoording van de vragen komen niet/nooit plotseling aspecten naar voren, die niet worden ondersteund/onderbouwd in de voorafgaande beschouwing.",
                "vragen": "",
            }
        },
    },
}

psychiatrie_interventieadvies = {
    "bestandsnaam": "BP_interventieadvies.docx",
    "titel": "Interventieadvies",
    "hoofdstukken": {
        
    },
}

psychiatrie_interventieadvies_complex = {
    "bestandsnaam": "BP_interventieadvies_complex.docx",
    "titel": "Interventieadvies",
    "subtitel": "Complexe problematiek",
    "hoofdstukken": {
        "Algemeen": {
            "Vraagstelling": {"verbergen": "ja"}
            },
        "Onderzoek": {
            "Speciële anamnese": {
                "toelichting":"We willen zicht krijgen op hoe betrokkene zelf het onderzoek ervaart, wat de hulpvraag van betrokkene zelf is en op welke manier betrokkene zijn/haar klachten, en de gevolgen daarvan ervaart. ",
                "Houding van betrokkene tegenover het onderzoek": "",
                "Toedracht van het onderzoek in de woorden van betrokkene": "",
                "Hulpvraag": {},
                "Door betrokkene ervaren klachten": "",
                "Door betrokkene ervaren beperkingen in het functioneren": "",
            },
            "Tractus anamnese":{
                "toelichting":"Vraag de volgende klachten uit, in de eigen woorden van betrokkene. Houd daarbij rekening met classificerende diagnostiek volgens de DSM-5-TR. Vraag bij herkenning van klachten telkens wanneer deze begonnen zijn, hoe het beloop is, welke factoren de klachten beïnvloeden en hoe ernstig deze zijn",
                "Bewustzijn":"",
                "Aandacht en concentratie":"",
                "Geheugen":"",
                "Waarneming":"",
                "Zelfwaarneming":"",
                "Inhoud van het denken":"",
                "Stemming":"",
                "Angsten":{"toelichting":"Vraag naar het type angst, lichamelijke sensaties en cognities. Bevraag ook paniek, dwanggedachten en dwanghandelingen"},
                "Slaap":{"toelichting":"Bevraag systematisch; hoe laat gaat betrokkene naar bed, hoe lang duurt het voor hij/zij in slaap valt, wordt hij/zij tussentijds wakker, zijn er problemen met te vroeg wakker worden?"},
                "Voeding en gewicht":"",
                "Trauma":{"toelichting":"Vraag naar gebeurtenissen die betrokkene als traumatisch heeft ervaren, geef eventueel een omschrijving van traumatische gebeurtenissen"},
                "Life-events":"",
                "Suïcidaliteit":{"toelichting":"Vraag hier concreet en rechtstreeks naar. Indien er sprake is van suïcidaliteit, hanteer dan de CASE-methodiek:\a1. Vraag naar de ruime voorgeschiedenis van suïcidaliteit - (langdurige kwetsbaarheid)\a2. Vraag naar relevante gebeurtenissen in de recente voorgeschiedenis - (stressor)\a3. Vraag naar actuele suïcidale gedachten, vraag naar de intensiteit, vraag naar plannen/voorbereidingen, vraag naar de bereidheid om die plannen uit te voeren of er juist van af te zien - (entrapment)\a4. Vraag naar de toekomst, zowel op korte als langere termijn; 'wat gaat u straks doen als u thuis bent?', 'hoe ziet u de toekomst op de langere termijn?' "},
                "Automutilatie":"",
                "Ander risico-gedrag":{"toelichting":"Dit kan betrekking hebben op andere vormen van gedrag die voor betrokkene of diens omgeving (inclusief degenen die aan zijn/haar zorg zijn toevertrouwd). Probeer te achterhalen of er sprake is of het gedrag doelgericht is en/of er sprake is van frustratie en/of er sprake is van acting-out. Taxeer risico's op dezelfde wijze als suïcidaliteit"},
                "Impulsbeheersing":""               
            },
            "Ontwikkelingsanamnese": {
                "toelichting":"Bij voorkeur hetero-anamnestisch afnemen bij een ouder/verzorger",
                "Perinatale periode": "",
                "Motoriek en spraak": "",
                "Zindelijkheid": "",
                "Sociale ontwikkeling": "",
                "Intellectuele ontwikkeling": "",
            },
            "Persoonlijkheidsfunctioneren":{
                "toelichting":"Het gaat hier om de beleving c.q. de ervaring van betrokkene zelf op deze domeinen. De beleving van betrokkene kan heel goed anders zijn dan je eigen observatie/inschatting/interpretatie of hypothese. Dat is niet erg maar dat wordt later op systematische wijze besproken, volsta hier gewoon met een 'zelfbeschrijving'.",
                "Identiteit": {"toelichting":"Heeft betrokkene een duidelijk gevoel van eigenheid en blijft dat behouden onder druk en onder stress? \aHeeft betrokkene een voldoende positief gevoel van eigenwaarde en is dat gevoel consistent met zelfverwezenlijking en kwaliteiten? Wat gebeurt er met dat gevoel onder stress? Wat is bepalend voor het gevoel van eigenwaarde?\aIs betrokkene in staat om het volledige palet aan emoties te ervaren? Is de intensiteit normaal, te hoog of te laag in relatie tot de onderliggende werkelijkheid? Is betrokkene in staat emoties geintegreerd te ervaren, is er ruimte voor nuance of is het zwart-wit?" },
                "Zelfsturing": {"toelichting":"Stelt betrokkene zichzelf doelen en zijn die doelen authentiek, persoonlijk en realistisch? Zet betrokkene ook realistische stappen om deze doelen te behalen?\aHeet betrokkene duidelijke normen en maatstaven waaraan hij/zij moet voldoen?Hoe gaat betrokkene met deze normen om? Streng/rigide of juist laks/passief?\aIs betrokkene in staat om over eigen mentale processen te reflecteren?"},
                "Empathie": {"toelichting":"Is betrokkene in staat om de gedachtengang van anderen te volgen en te begrijpen? Is betrokkene erg gevoelig voor bepaalde emoties bij anderen? Kleurt dit de vermeende intenties van anderen?\aKan betrokkene inzien dat anderen een andere visie op iets hebben? Hoe ervaart betrokkene een verschil van mening met anderen?\aKan betrokkene begrijpen en inschatten welke impact hij/zij op anderen heeft?"},
                "Intimiteit": {"toelichting":"Is betrokkene in staat tot positieve verbondenheid met anderen? Is verbondenheid stabiel en langdurig positief?\aHeeft betrokkene een capaciteit to intieme/nabije verbondenheid? Is er sprake van wederkerigheid (i.e. wederzijdse waardering maar ook het vermogen om afhankelijkheid en kwetsbaarheid te verdragen)?\aIs betrokkene in staat tot constructieve samenwerking?"},                
        },
        },
        "Bespreking": {
            "Beschrijvende diagnose": {
                "Context": {},
                "Klachten en symptomen die op de voorgrond staan:": {},
                "Hypothese over het toestandsbeeld": {},
                "Hypothese over beïnvloedende factoren": {},
            },
            "Classificerende diagnose": {},
            "Differentiaal diagnostische overwegingen": {},
            "Advies voor inzet van interventie": {
                "Belangrijkste focus voor interventie": {},
                "Type interventie of behandeling": {},
                "Echelon op basis van complexiteit,ernst,comorbiditeit en risico's": {},
                "Inschatting van de duur en intensiteit van interventie of behandeling": {},
                "Advies": {},
            },
            "DSM-5-TR": {},
        },
        "Beantwoording vraagstelling": {"verbergen": "ja"},
    },
}


def get_report():
    reports = [
        [basis_rapport],
        [basis_rapport, basis_rapport_psychiatrie],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_interventieadvies_complex,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_interventieadvies_complex,
            psychiatrie_interventieadvies,
        ],
        [basis_rapport, basis_rapport_psychiatrie, psychiatrie_belastbaarheid],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_belastbaarheid,
            arbeidsrecht_belastbaarheid,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_belastbaarheid,
            bestuurssrecht_belastbaarheid,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            icara_belastbaarheid,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_belastbaarheid,
            AOV_belastbaarheid,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_belastbaarheid,
            IGJ_belastbaarheid,
        ],
        [basis_externe_info],
    ]
    context = []
    for report in reports:
        context.append(merge_reports(report))
    return context


def merge(source, extension):
    source = copy.deepcopy(source)
    for k, v in source.items():
        try:
            if k in extension.keys():
                if not isinstance(extension[k], dict):
                    source[k] = extension[k]
                elif v == {}:
                    source[k] = extension[k]
                elif (
                    hasattr(v, "values")
                    and callable(v.values)
                    and not any(isinstance(value, dict) for value in v.values())
                ):
                    source[k] = extension[k]
                else:
                    source[k] = merge(source[k], extension[k])
        except Exception as e:
            print(
                f"\nexception {e} \n\nsource k:v {k} : {v}\n\n extension {extension}\n\n"
            )
            raise

    return source


def merge_reports(reports):
    while len(reports) > 1:
        reports[1] = merge(reports[0], reports[1])
        reports = reports[1:]
    if len(reports) == 1:
        pprint(reports[0])
        return reports[0]
    pass


if __name__ == "__main__":
    print("\n")
    reports = [basis_rapport, basis_rapport_psychiatrie, arbeidsrecht_belastbaarheid]
    merge_reports(reports)
