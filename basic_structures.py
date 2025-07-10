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
    "IA": {
        "Context": {
            "toelichting": context_algemene_toelichting,
            "tekst": "De rapportage wordt in een arbeidsrechtelijk kader uitgevoerd op verzoek van de werkgever c.q. de bedrijfsarts van betrokkene. Het doel van het onderzoek is de bedrijfsarts te informeren over de inzet van interventie en/of behandeling met als doel duurzame inzetbaarheid van betrokkene die werknemer is",
        },
        "Correcties": correcties_algemeen,
        "Inzage- en blokkering": "Het inzage- en blokkeringsrecht zijn van toepassing. Betrokkene heeft op [DATUM] ter inzage het definitieve rapport toegestuurd gekregen. Aan betrokkene werd daarbij verzocht om voor [DATUM_2] kenbaar te maken of hij/zij akkoord gaat met verzending van de rapportage.\nBetrokkene reageerde op [DATUM_3] op dit verzoek en gaf daarbij aan dat het rapport WEL/NIET geblokkeerd was. Het rapport is daartoe [NIET VERZONDEN/VERZONDEN AAN DE OPDRACHTGEVER OP DATUM_4]\nBetrokkene reageerde niet binnen de daartoe afgesproken termijn, het rapport wordt daarom als geblokkeerd beschouwd en opdrachtgever werd daarvan op [DATUM_4] op de hoogte gesteld.",
        "Commentaar": commentaar_algemeen,
    },
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

FML = {
    "bestandsnaam": "FML.docx",
    "voorblad": "yes",
    "titel": "Functionele mogelijkheden lijst",
    "hoofdstukken": {
        "Algemeen": {
            "Functionele mogelijkheden lijst": {
                "tekst": "Deze lijst geeft een overzicht van mogelijkheden om in het algemeen gedurende een hele werkdag (ten minste 8 uur) te functioneren. Beperkingen van deze mogelijkheden ten opzichte van de referentiewaarden worden in aparte rubrieken weergegeven, voor zover deze naar het oordeel van de verzekeringsarts uitingen zijn van ziekten, gebreken of ongeval/en. Als referentiewaarden zijn die niveaus van functioneren gekozen die het dagelijks leven regelmatig vereist. Tenzij uitdrukkelijk anders vermeld, is een incidentele piekbelasting of structureel marginaal hogere belasting eveneens mogelijk boven zowel de referentiewaarde als de aangenomen beperkte functionele mogelijkheden. Deze lijst is niet geschikt voor toepassing los van een verzekeringsgeneeskundige rapportage waarin de mogelijkheden en beperkingen aan de hand van een probleemanalyse in hun onderlinge samenhang beoordeeld, gemotiveerd en beschreven zijn."
            },
            "Conclusie": {
                "tekst": "De cliënt beschikt over duurzaam benutbare mogelijkheden.\aDe client beschikt niet over duurzaam benutbare mogelijkheden."
            },
            "Toelichting": {
                "tekst": "De client is in staat om het eigen werk volledig uit te voeren.\aDe client is in staat tot functioneren volgens de referentiewaarden (zie rubrieken).\aDe cliënt heeft beperkingen t.o.v. functioneren volgens de referentiewaarde (zie rubrieken).\aAnders, zie rapportage verzekeringsarts.\aDe client disfunctioneert persoonlijk en sociaal a.g.v. een ernstige psychische stoornis.\aDe cliënt is opgenomen in ziekenhuis of Wlz-erkende instelling.De cliënt is bedlegerig (grootste deel van de dag en langdurig).\aDe cliënt is in grote mate ADL-afhankelijk.\aDe cliënt heeft sterk wisselende mogelijkheden/verlies van mogelijkheden (< 3 mnd-1 jr)"
            },
            "Duurzaamheid arbeidsbeperking": {"tekst": " "},
            "Algemene opmerkingen": {"tekst": "Opgesteld op [...]\aGeldig per [...]"},
        },
        "Rubriek I - Persoonlijk functioneren": {
            "1. Vasthouden van de aandacht (concentreren) in het dagelijks functioneren": {
                "tekst": 
"""0   Norm. Kan de aandacht tenminste een half uur richten op één informatiebron.
1   Beperkt. Kan de aandacht niet langer dan een half uur richten op één informatiebron.
2   Sterk beperkt. Kan de aandacht niet langer dan 5 minuten richten op één informatiebron."""
            },
            "2. Verdelen van de aandacht in het dagelijks functioneren":{ 
                "tekst":
"""0   Norm. Kan de aandacht alternerend richten op meerdere uiteenlopende informatiebronnen (verkeersdeelname met een voertuig).
1   Beperkt. Kan de aandacht alternerend richten op een beperkt aantal informatiebronnen (reizen met het OV).
2   Sterk beperkt. Kan niet of nauwelijks de aandacht alternerend richten op uiteenlopende informatiebronnen."""},
            "3. Herinneren in het dagelijks functioneren":{
                "tekst":
"""0   Norm. Kan zich doorgaans tijdig, zonder ongebruikelijke hulpmiddelen, relevante zaken herinneren.
1    Beperkt. Moet regelmatig dingen apart opschrijven als geheugensteun om de continuïteit van handelen te waarborgen.
2    Sterk beperkt. Weet zich onontbeerlijke alledaagse gegevens (tijd/plaats/persoon/onderwerp) niet te  herinneren en kan dit niet compenseren met hulpmiddelen."""},
            "4. Inzicht in eigen kunnen in het dagelijks functioneren":{
                "tekst":
"""0   Norm. Schat doorgaans de eigen mogelijkheden en beperkingen realistisch in.
1   Beperkt. Overschat doorgaans ernstig de eigen mogelijkheden.
2   Beperkt. Overschat doorgaans ernstig de eigen beperkingen."""},
            "5 Doelmatig handelen (taakuitvoering) in het dagelijks functioneren":{
                "tekst": 
"""0   Norm. Geen specifieke beperkingen in doelmatig handelen in de routine in het dagelijks functioneren.
1   Beperkt: start niet tijdig activiteiten om het gestelde doel te bereiken.
2   Beperkt: voert de benodigde activiteiten niet in een logische volgorde uit..
3   Beperkt: controleert het verloop van de activiteiten niet.
4   Beperkt: beëindigt de activiteiten niet als het gestelde doel bereikt is of niet bereikt kan worden.
5   Anderszins beperkt in doelmatig handelen, namelijk:"""},
             "6.  Zelfstandig handelen in het dagelijks functioneren":{ 
                 "tekst":
"""0   Norm. Geen specifieke beperkingen in het zelfstandig handelen in het dagelijks leven.
1   Beperkt: neemt doorgaans niet uit zichzelf het initiatief tot handelen.
2   Beperkt: stelt zichzelf doorgaans geen doelen.
3   Beperkt: ontwerpt zelf doorgaans geen oplossingsvarianten.
4   Beperkt: besluit doorgaans zelf niet welke aanpak de meest geëigende is.
5   Beperkt: onderkent zelf doorgaans niet wanneer de gevolgde aanpak tekort schiet.
6   Beperkt: kiest in dat geval doorgaans niet zelf voor een alternatieve aanpak of een ander doel.
7   Beperkt: gaat uit zichzelf doorgaans niet door totdat het doel bereikt is.
8   Beperkt: doet zelf niet tijdig een beroep op de hulp van anderen, wanneer de situatie dat gebiedt.
9   Anderszins beperkt in zelfstandig handelen, namelijk:"""},
             "7. Handelingstempo in het dagelijks functioneren":{ 
                 "tekst":
"""0   Norm. Er zijn geen specifieke beperkingen in handelingstempo in het dagelijks functioneren.
1   Beperkt. Het handelingstempo is aanmerkelijk vertraagd."""},
             "8. Specifieke voorwaarden voor het persoonlijk functioneren in arbeid – is het functioneren in arbeid door de genoemde beperkingen, of het daarop gerichte compensatiegedrag, afhankelijk van specifieke voorwaarden?":{ 
                 "tekst":
"""0   Nee. Geen specifieke voorwaarden voor het persoonlijk functioneren in arbeid.
1   Ja: aangewezen op werk met niet of nauwelijks afleiding door activiteiten van anderen; namelijk ….
2   Ja: aangewezen op een voorspelbare werksituatie, kan niet of nauwelijks flexibel inspelen op sterk wisselende uitvoeringsomstandig-heden en/of taakinhoud; namelijk: …
3   Ja: werksituatie zonder veelvuldige storingen/onderbrekingen; namelijk: …
4   Ja: werk zonder veelvuldige deadlines of productiepieken; namelijk: …
5   Ja: werk waarin geen hoog handelingstempo vereist is; namelijk: …
6   Ja: werk zonder verhoogd persoonlijk risico; namelijk: …
7   Ja, er gelden overige specifieke voorwaarden voor persoonlijk functioneren, namelijk:"""},
             
            "9. Mate van zelfstandigheid":{ 
                "tekst":
"""0   Norm. Geen beperkingen.
1   Beperkt, is aangewezen op vaste/bekende werkwijzen.
2   Sterk beperkt, is aangewezen op volledig voorgestructureerd werk."""}
        },
        "Rubriek II - Sociaal functioneren": {
            "1. Zien":{ 
                "tekst":
"""0   Norm. Geen specifieke beperkingen in het dagelijks functioneren.
1   Beperkt, namelijk:"""},
"2. Horen":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen in het dagelijks functioneren.
1   Beperkt, namelijk:"""},
"3.  Spreken":{ 
    "tekst": 
"""0   Norm. Geen specifieke beperkingen in het dagelijks functioneren.
1   Beperkt, namelijk:"""} ,
"4. Schrijven":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen in het dagelijks functioneren.
1   Beperkt, namelijk:"""},
"5. Lezen":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen in het dagelijks functioneren.
1   Beperkt, namelijk:"""},
"6. Emotionele problemen van anderen hanteren":{ 
    "tekst":
"""0   Norm. Kan zich doorgaans inleven in problemen van anderen, maar kan daarvan ook afstand nemen in gedrag en beleving.
1   Beperkt. Trekt zich doorgaans problemen van anderen erg aan; kan desondanks wel voldoende afstand nemen in gedrag, echter niet in beleving:
2   Beperkt. Trekt zich doorgaans problemen van anderen onvoldoende aan; kan zich desondanks wel enigszins inleven in anderen en hen bijstaan/ondersteunen:
3   Sterk beperkt. Trekt zich doorgaans problemen van anderen erg aan en kan daarvan noch in gedrag noch in beleving afstand nemen:
4   Sterk beperkt. Trekt zich doorgaans problemen van anderen onvoldoende aan, kan zich niet inleven in anderen en hen ook niet bijstaan/ondersteunen:"""},
"7. Eigen gevoelens uiten":{ 
    "tekst": 
"""0    Norm. Kan doorgaans persoonlijke gevoelens op een voor anderen duidelijke/acceptabele manier in woord en gedrag tot uiting brengen.
1   Beperkt. Is doorgaans niet in staat gevoelens te uiten (blokkeert zichzelf): …
2   Beperkt. Brengt anderen in verwarring door onduidelijke/onvoorspelbare/onconventionele wijzen van gevoelsuitingen: …
3   Beperkt. Uit gevoelens op een ongecontroleerde (ongeremde) wijze:"""},
"8. Omgaan met conflicten":{ 
    "tekst":
"""0   Norm. Geen specifieke beperking.
1   Beperkt. Kan een conflict met agressieve/onredelijke mensen uitsluitend in telefonisch of schriftelijk contact hanteren. 
2   Sterk beperkt. Kan doorgaans geen conflicten hanteren."""},
"9. Samenwerken":{
    "tekst":
"""0    Norm. Kan in onderlinge afstemming met anderen een taak gezamenlijk uitvoeren (werken in teamverband).
1    Beperkt. Kan met anderen samenwerken, maar met een eigen, van tevoren afgebakende deeltaak. 
2    Sterk beperkt. Kan doorgaans niet met anderen samenwerken."""}, 
"10. Vervoer":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen. Kan zelfstandig reizen; autorijden, fietsen (verkeersdeelname) of zelfstandig gebruik maken van het openbaar vervoer.
1   Beperkt. Kan niet zelfstandig reizen, namelijk:"""}, 
"11. Beroepsmatig vervoer":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt. Kan niet of beperkt beroepsmatig een voertuig besturen; namelijk:"""},
"12. Specifieke voorwaarden voor het sociaal functioneren in arbeid – is het sociaal functioneren door de genoemde  beperkingen, of het daarop gerichte compensatiegedrag, afhankelijk van specifieke voorwaarden?":{ 
    "tekst":
"""0   Nee. Geen specifieke voorwaarden voor het sociaal functioneren in arbeid.
1   Ja: aangewezen op werk waarin doorgaans weinig of geen rechtstreeks contact met klanten vereist is; namelijk:
2   Ja: aangewezen op werk waarin doorgaans weinig of geen direct contact met patiënten of hulpbehoevenden vereist is; namelijk:
3   Ja: aangewezen op werk waarin z.n. kan worden teruggevallen op directe collega’s/leidinggevenden (geen solitaire functie).
4   Ja: aangewezen op werk waarin doorgaans geen direct contact met collega’s is vereist.
5   Ja: aangewezen op werk dat geen leidinggevende aspecten bevat; namelijk: 
6   Ja, er gelden overige specifieke voorwaarden, namelijk; namelijk:"""}

            },
        "Rubriek III - Aanpassingen aan fysieke omgevingseisen": {
            "1. Temperatuur":{ 
                "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt. Hitte is beperkt (>35ºC).
2   Beperkt. Koude is beperkt (< -15ºC)."""},
"2. Tocht":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"3. Huidcontact":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"4. Beschermende middelen":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"5. Stof, rook, gassen en/of dampen":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"6. Geluidsbelasting":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"7. Trillingsbelasting":{ 
    "tekst":
"""0   Norm. Geen specifieke beperkingen.
1   Beperkt, namelijk:"""},
"8. Overige beperkingen van fysieke aanpassingsmogelijkheden":{ 
    "tekst":
"""0   Norm. Geen specifieke overige beperkingen in fysieke aanpassingsmogelijkheden.
1   Ja: allergie:
2   Ja: verhoogde vatbaarheid voor infecties:
3   Ja: verzwakte huidbarrière:
4   Ja: andere beperkingen, te weten:"""}
},
        "Rubriek IV - Dynamische handelingen": {
    "1. Dominantie": {
        "tekst": "0   Niet van toepassing\n1   Rechts\n2   Links"
    },
    "2. Localisatie beperkingen": {
        "tekst": "0   Niet van toepassing\n1   Rechts\n2   Links\n3   Tweezijdig"
    },
    "3. Hand- en vingergebruik": {
        "tekst": "0   Norm. Geen specifieke beperkingen bij het gebruik van handen en vingers in het dagelijks functioneren.\n1   De bolgreep is beperkt; namelijk:\n2   De pengreep is beperkt; namelijk:\n3   De pincetgreep is beperkt; namelijk:\n4   De sleutelgreep is beperkt; namelijk:\n5   De cilindergreep is beperkt; namelijk:\n6   Knijp/grijpkracht is beperkt; namelijk:\n7   Fijn-motorische hand-/vingerbewegingen zijn beperkt; namelijk:\n8   Repetitieve hand-/vingerbewegingen zijn beperkt; namelijk:\n9   Toetsenbord bedienen en muis hanteren is beperkt; namelijk:"
    },
    "4. Werken met toetsenbord en/of muis": {
        "tekst": "0   Norm. Kan zo nodig gedurende het merendeel van de werkdag een met een toetsenbord en/of muis werken.\n1   Licht beperkt. Kan zo nodig gedurende de helft van de werkdag (ongeveer 4 uur) met een toetsenbord en/of muis werken.\n2   Beperkt. Kan zo nodig gedurende een beperkt deel van de werkdag (ongeveer 1 uur) met een toetsenbord en/of muis werken.\n3   Sterk beperkt. Kan gedurende minder dan een half uur per werkdag met een toetsenbord en/of muis werken."
    },
    "5. Tastzin": {
        "tekst": "0   Norm. Geen specifieke beperkingen.\n1   Beperkt, namelijk:"
    },
    "6. Schroefbewegingen met hand en arm": {
        "tekst": "0   Norm. Geen specifieke beperkingen.\n1   Beperkt, namelijk:"
    },
    "7. Reiken": {
        "tekst": "0   Norm. Maximale reikafstand is 70cm.\n1   Licht beperkt. Maximale reikafstand is 60 cm.\n2   Beperkt. Maximale reikafstand is 50 cm."
    },
    "8. Frequent reiken tijdens werk": {
        "tekst": "0   Norm. Kan zo nodig tijdens elk uur van de werkdag 1200x (20x/min) reiken.\n1   Beperkt. Kan zo tijdens elk uur van de werkdag ongeveer 600x reiken.\n2   Sterk beperkt. Kan zo nodig tijdens elk uur van de werkdag ongeveer 300x reiken."
    },
    "9. Buigen": {
        "tekst": "0   Norm. Kan ongeveer 90 graden buigen.\n1   Beperkt. Kan ongeveer 60 graden buigen.\n2   Sterk beperkt. Kan ongeveer 45 graden buigen."
    },
    "10. Frequent buigen tijdens werk": {
        "tekst": "0   Norm. Kan zo tijdens elk uur van de werkdag ongeveer 600x buigen.\n1   Licht beperkt. zo tijdens elk uur van de werkdag ongeveer 300x buigen.\n2   Beperkt. zo tijdens elk uur van de werkdag ongeveer 150x buigen.\n3   Sterk beperkt. zo tijdens elk uur van de werkdag ongeveer 50x buigen."
    },
    "11. Torderen": {
        "tekst": "0   Norm. Kan de romp ten minste 45 graden draaien in zittende houding, met gefixeerd bekken.\n1   Beperkt, namelijk: ..."
    },
    "12. Duwen of trekken": {
        "tekst": "0   Norm. Kan ongeveer 250N (25 kgF) duwen of trekken.\n1   Beperkt. Kan ongeveer 150N (15 kgF) duwen of trekken.\n2   Sterk beperkt. Kan ongeveer 100N (10 kgF) duwen of trekken."
    },
    "13. Tillen": {
        "tekst": "0   Norm. Kan ongeveer 15 kg tillen (t/m 10x/u).\n1   Licht beperkt. Kan ongeveer 10 kg tillen (t/m 10x/u).\n2   Beperkt. Kan ongeveer 5 kg tillen (t/m 50x/u).\n3   Sterk beperkt. Kan ongeveer 2 kg tillen (t/m 100x/u)."
    },
    "14. Dragen": {
        "tekst": "0   Norm. Kan ongeveer 15 kg dragen (t/m 4’ aaneen).\n1   Licht beperkt. Kan ongeveer 10 kg dragen (t/m 2’ aaneen).\n2   Beperkt. Kan ongeveer 5 kg dragen (t/m 1’ aaneen).\n3   Sterk beperkt. Kan ongeveer 2 kg dragen (t/m 2’ aaneen indien t/m 5x/u; 1’ indien>5x/u)."
    },
    "15. Hoofdbewegingen maken": {
        "tekst": "0   Norm. Kan het hoofd ongehinderd bewegen (120x/u).\n1   Beperkt. Kan het hoofd beperkt bewegen, namelijk: ...\n2   Sterk beperkt: kan het hoofd niet of nauwelijks bewegen, namelijk ..."
    },
    "16. Lopen": {
        "tekst": "0   Norm. Kan ongeveer een uur achtereen lopen (3 km/u).\n1   Licht beperkt. Kan ongeveer 30 minuten achtereen lopen.\n2   Beperkt. Kan ongeveer 15 minuten achtereen lopen.\n3   Sterk beperkt. Kan minder dan ongeveer 5 minuten achtereen lopen."
    },
    "17. Lopen tijdens het werk": {
        "tekst": "0   Norm. Kan zo nodig gedurende het merendeel van de werkdag lopen (3km/u).\n1   Licht beperkt. Kan zo nodig gedurende de helft van de werkdag (ongeveer 4 uur) lopen.\n2   Beperkt. Kan zo nodig gedurende een beperkt deel van de werkdag (ongeveer 1 uur) lopen.\n3   Sterk beperkt. Kan gedurende minder dan een half uur per werkdag lopen."
    },
    "18. Trappenlopen": {
        "tekst": "0   Norm. Kan ten minste in één keer 2 trappen op en af (totaal 60 treden).\n1   Licht beperkt. Kan ten minste in één keer 1 trap op en af (totaal 30 treden).\n2   Beperkt. Kan in één keer 1 trap op òf af (totaal 15 treden).\n3   Sterk beperkt. Kan in één keer slechts een bordestrapje op- of aflopen."
    },
    "19. Klimmen": {
        "tekst": "0   Norm. Kan ten minste een ladder op en af (gemiddeld 5m).\n1   Licht beperkt. Kan ten minste een huishoudtrap op en af (gemiddeld 3 meter).\n2   Beperkt. Kan ten minste een opstapje op en af.\n3   Sterk beperkt. Kan geen opstap maken."
    },
    "20. Knielen en/of hurken": {
        "tekst": "0   Norm. Kan 10x/u knielend of hurkend met de handen de grond bereiken.\n1   Licht beperkt. Kan hooguit 5x/u knielend en/of hurkend met de handen de grond bereiken.\n2   Beperkt. Kan hooguit 2x/u knielend en/of hurkend met de handen de grond bereiken.\n3   Sterk beperkt. Kan niet of nauwelijks knielend en/of hurkend met de handen de grond bereiken."
    },
    "21. Overige beperkingen van dynamisch handelen": {
        "tekst": "0   Norm. Geen specifieke overige beperkingen in dynamisch handelen.\n1   Ja, er gelden specifieke overige beperkingen, namelijk: ..."
    }
},

"Rubriek V - Statische houdingen": {
    "1. Zitten": {
        "tekst": "0   Norm. Kan ongeveer 2 uur achtereen zitten.\n1   Licht beperkt. Kan ongeveer een uur achtereen zitten.\n2   Beperkt. Kan ongeveer een half uur  achtereen zitten.\n3   Sterk beperkt. Kan minder dan een kwartier achtereen zitten."
    },
    "2. Zitten tijdens het werk": {
        "tekst": "0   Norm. Kan zo nodig gedurende vrijwel de gehele werkdag zitten.\n1   Licht beperkt. Kan zo nodig gedurende het grootste deel van de werkdag zitten (niet meer dan 8 uur).\n2   Beperkt. Kan zo nodig gedurende de helft van de werkdag (ongeveer 4 uur) zitten.\n3   Sterk beperkt. Kan minder dan 4 uur per werkdag zitten."
    },
    "3. Staan": {
        "tekst": "0   Norm. Kan ongeveer een uur achtereen staan.\n1   Licht beperkt. Kan ongeveer een half uur achtereen staan.\n2   Beperkt. Kan ongeveer 15 minuten achtereen staan.\n3   Sterk beperkt. Kan minder dan 5 minuten achtereen staan."
    },
    "4. Staan tijdens het werk": {
        "tekst": "0   Norm. Kan zo nodig gedurende het merendeel van de werkdag staan.\n1   Licht beperkt. Kan zo nodig gedurende de helft van de werkdag staan (ongeveer 4 uur).\n2   Beperkt. Kan zo nodig gedurende een beperkt deel van de werkdag (ongeveer 1 uur) staan.\n3   Sterk beperkt. Kan minder dan een half uur per werkdag staan."
    },
    "5. Geknield of gehurkt actief zijn": {
        "tekst": "0   Norm. Kan dit ten minste 5 minuten achtereen (2x/u).\n1   Beperkt. Kan dit minder dan 5 minuten achtereen; te weten: ..."
    },
    "6. Gebogen en/of getordeerd actief zijn": {
        "tekst": "0   Norm. Kan dit 5 minuten of meer achtereen (2x/u).\n1   Beperkt. Kan dit tot 5 minuten achtereen.\n2   Sterk beperkt. Kan dit tot 2 minuten achtereen."
    },
    "7. Boven schouderhoogte actief zijn": {
        "tekst": "0   Norm. Kan dit 2 minuten achtereen (10x/u).\n1   Beperkt. Kan dit ongeveer 1 minuut achtereen; namelijk: …\n2   Sterk beperkt. Kan dit niet of nauwelijks; namelijk: …"
    },
    "8. Het hoofd in een bepaalde stand houden": {
        "tekst": "0   Norm. Kan dit zo nodig gedurende het merendeel van de werkdag.\n1   Licht beperkt. Kan dit zo nodig gedurende de helft van de werkdag (ongeveer 4 uur).\n2   Beperkt. Kan dit zo nodig gedurende een beperkt deel van de werkdag (ongeveer 1 uur).\n3   Sterk beperkt. Kan dit minder dan een half uur per werkdag."
    },
    "9. Afwisseling van houding": {
        "tekst": "0   Norm. Geen specifieke opeenvolging van verschillende houdingen vereist.\n1   Beperkt. Specifieke afwisseling van houdingen vereist, namelijk: ..."
    },
    "10. Overige beperkingen van statische houdingen": {
        "tekst": "0   Norm. Geen specifieke overige beperkingen m.b.t. statische houdingen.\n1   Ja, er gelden specifieke overige beperkingen, namelijk: ..."
    }
},
"Rubriek VI - Werktijden": {
    "1. Perioden van het etmaal": {
        "tekst": "0   Norm. Kan zo nodig op elk uur van het etmaal werken, ook ‘s nachts.\n1   Beperkt. Kan niet elke avond werken (18:00 – 22:00 u), namelijk: ...\n2   Beperkt. Kan ‘s nachts niet werken (22:00 – 6:00 u)"
    },
    "2. Uren per dag": {
        "tekst": "0   Norm. Kan gemiddeld ten minste 8 uur per dag werken.\n1   Enigszins beperkt. Kan gemiddeld ongeveer 8 uur per dag werken.\n2   Licht beperkt. Kan gemiddeld ongeveer 6 uur per dag werken, namelijk: ...\n3   Beperkt. Kan gemiddeld ongeveer 4 uur per dag werken, namelijk: ...\n4   Zeer beperkt. Kan gemiddeld ongeveer 2 uur per dag werken, namelijk: ..."
    },
    "3. Uren per week": {
        "tekst": "0   Norm. Kan gemiddeld tenminste 40 uur per week werken.\n1   Enigszins beperkt. Kan gemiddeld ongeveer 40 uur per week werken.\n2   Licht beperkt. Kan gemiddeld ongeveer 30 uur per week werken, namelijk: ...\n3   Beperkt. Kan gemiddeld ongeveer 20 uur per week werken, namelijk: ...\n4   Zeer beperkt. Kan gemiddeld ongeveer 10 uur per week werken, namelijk: ..."
    },
    "4. Overige beperkingen ten aanzien van werktijd": {
        "tekst": "0   Norm. Geen specifieke overige beperkingen ten aanzien van werktijden.\n1   Ja, er gelden specifieke overige beperkingen, namelijk: ..."
    }
}

    },
}

temp = """"
            
            
             ...
            ... 
            
            """


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
        "Advies voor interventie": {"verbergen": "ja"},
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
            "Persoonlijkheidsfunctioneren": {"verbergen": "ja"},
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
        "Algemeen": {
            "Context": contexten["IA"]["Context"],
            "Correcties": {"tekst": contexten["IA"]["Correcties"]},
            "Inzage- en blokkering": {
                "tekst": contexten["IA"]["Inzage- en blokkering"]
            },
            "Commentaar": {"tekst": contexten["IA"]["Commentaar"]},
            "Vraagstelling": {"verbergen": "ja"},
        },
        "Onderzoek": {
            "Speciële anamnese": {
                "toelichting": "We willen zicht krijgen op hoe betrokkene zelf het onderzoek ervaart, wat de hulpvraag van betrokkene zelf is en op welke manier betrokkene zijn/haar klachten, en de gevolgen daarvan ervaart. ",
                "Houding van betrokkene tegenover het onderzoek": "",
                "Toedracht van het onderzoek in de woorden van betrokkene": "",
                "Hulpvraag": {},
                "Door betrokkene ervaren klachten": "",
                "Door betrokkene ervaren beperkingen in het functioneren": "",
            },
            "Tractus anamnese": {
                "toelichting": "Vraag de volgende klachten uit, in de eigen woorden van betrokkene. Houd daarbij rekening met classificerende diagnostiek volgens de DSM-5-TR. Vraag bij herkenning van klachten telkens wanneer deze begonnen zijn, hoe het beloop is, welke factoren de klachten beïnvloeden en hoe ernstig deze zijn",
                "Bewustzijn": "",
                "Aandacht en concentratie": "",
                "Geheugen": "",
                "Waarneming": "",
                "Zelfwaarneming": "",
                "Inhoud van het denken": "",
                "Stemming": "",
                "Angsten": {
                    "toelichting": "Vraag naar het type angst, lichamelijke sensaties en cognities. Bevraag ook paniek, dwanggedachten en dwanghandelingen"
                },
                "Slaap": {
                    "toelichting": "Bevraag systematisch; hoe laat gaat betrokkene naar bed, hoe lang duurt het voor hij/zij in slaap valt, wordt hij/zij tussentijds wakker, zijn er problemen met te vroeg wakker worden?"
                },
                "Voeding en gewicht": "",
                "Trauma": {
                    "toelichting": "Vraag naar gebeurtenissen die betrokkene als traumatisch heeft ervaren, geef eventueel een omschrijving van traumatische gebeurtenissen"
                },
                "Life-events": "",
                "Suïcidaliteit": {
                    "toelichting": "Vraag hier concreet en rechtstreeks naar. Indien er sprake is van suïcidaliteit, hanteer dan de CASE-methodiek:\a1. Vraag naar de ruime voorgeschiedenis van suïcidaliteit - (langdurige kwetsbaarheid)\a2. Vraag naar relevante gebeurtenissen in de recente voorgeschiedenis - (stressor)\a3. Vraag naar actuele suïcidale gedachten, vraag naar de intensiteit, vraag naar plannen/voorbereidingen, vraag naar de bereidheid om die plannen uit te voeren of er juist van af te zien - (entrapment)\a4. Vraag naar de toekomst, zowel op korte als langere termijn; 'wat gaat u straks doen als u thuis bent?', 'hoe ziet u de toekomst op de langere termijn?' "
                },
                "Automutilatie": "",
                "Ander risico-gedrag": {
                    "toelichting": "Dit kan betrekking hebben op andere vormen van gedrag die voor betrokkene of diens omgeving (inclusief degenen die aan zijn/haar zorg zijn toevertrouwd). Probeer te achterhalen of er sprake is of het gedrag doelgericht is en/of er sprake is van frustratie en/of er sprake is van acting-out. Taxeer risico's op dezelfde wijze als suïcidaliteit"
                },
                "Impulsbeheersing": "",
            },
        },
        "Bespreking": {
            "Beschrijvende diagnose": {},
            "Classificerende diagnose": {},
            "DSM-5-TR": {},
            "Differentiaal diagnostische overwegingen": {},
        },
        "Beantwoording vraagstelling": {"verbergen": "ja"},
        "Advies voor interventie": {
            "Belangrijkste focus voor interventie": {},
            "Type interventie of behandeling": {},
            "Echelon op basis van complexiteit,ernst,comorbiditeit en risico's": {},
            "Inschatting van de duur en intensiteit van interventie of behandeling": {},
            "Advies": {},
        },
    },
}

psychiatrie_interventieadvies_kort = {
    "bestandsnaam": "BP_interventieadvies_kort.docx",
    "titel": "Interventieadvies",
    "subtitel": "",
    "hoofdstukken": {
        "Onderzoek": {
            "Ontwikkelingsanamnese": {"verbergen": "ja"},
            "Persoonlijkheidsfunctioneren": {"verbergen": "ja"},
        },
        "Bespreking": {
            "Beschrijvende diagnose": {
                "Door betrokkene ervaren klachten en beperkingen": {
                    "toelichting": "Bespreek hier zowel hetgeen betrokkene anamnestisch heeft vermeld."
                },
                "Geobserveerde symptomen": {
                    "toelichting": "Beschrijf hier de tijdens het onderzoek geobserveerde afwijkingen zoals die bijvoorbeeld blijken bij het psychiatrisch onderzoek. Bespreek hier ook eventueel heteroanamnestische informatie en objectieve informatie uit andere bronnen"
                },
                "Hypothese over het persoonlijkheidsfunctioneren": {
                    "toelichting": "Beschrijf hier kort of er sprake lijkt te zijn van patroonmatige symptomatologie en/of problemen in het persoonlijkheidsfunctioeren"
                },
                "Hypothese over beïnvloedende factoren": {},
                "Hypothese over het toestandsbeeld": {},
            },
        },
    },
}

psychiatrie_interventieadvies_complex = {
    "bestandsnaam": "BP_interventieadvies_complex.docx",
    "titel": "Interventieadvies",
    "subtitel": "Complexe problematiek",
    "hoofdstukken": {
        "Algemeen": {"Vraagstelling": {"verbergen": "ja"}},
        "Onderzoek": {
            "Ontwikkelingsanamnese": {
                "toelichting": "Bij voorkeur hetero-anamnestisch afnemen bij een ouder/verzorger",
                "Perinatale periode": "",
                "Motoriek en spraak": "",
                "Zindelijkheid": "",
                "Sociale ontwikkeling": "",
                "Intellectuele ontwikkeling": "",
            },
            "Persoonlijkheidsfunctioneren": {
                "toelichting": "Het gaat hier om de beleving c.q. de ervaring van betrokkene zelf op deze domeinen. De beleving van betrokkene kan heel goed anders zijn dan je eigen observatie/inschatting/interpretatie of hypothese. Dat is niet erg maar dat wordt later op systematische wijze besproken, volsta hier gewoon met een 'zelfbeschrijving'.",
                "Identiteit": {
                    "toelichting": "Heeft betrokkene een duidelijk gevoel van eigenheid en blijft dat behouden onder druk en onder stress? \aHeeft betrokkene een voldoende positief gevoel van eigenwaarde en is dat gevoel consistent met zelfverwezenlijking en kwaliteiten? Wat gebeurt er met dat gevoel onder stress? Wat is bepalend voor het gevoel van eigenwaarde?\aIs betrokkene in staat om het volledige palet aan emoties te ervaren? Is de intensiteit normaal, te hoog of te laag in relatie tot de onderliggende werkelijkheid? Is betrokkene in staat emoties geintegreerd te ervaren, is er ruimte voor nuance of is het zwart-wit?"
                },
                "Zelfsturing": {
                    "toelichting": "Stelt betrokkene zichzelf doelen en zijn die doelen authentiek, persoonlijk en realistisch? Zet betrokkene ook realistische stappen om deze doelen te behalen?\aHeet betrokkene duidelijke normen en maatstaven waaraan hij/zij moet voldoen?Hoe gaat betrokkene met deze normen om? Streng/rigide of juist laks/passief?\aIs betrokkene in staat om over eigen mentale processen te reflecteren?"
                },
                "Empathie": {
                    "toelichting": "Is betrokkene in staat om de gedachtengang van anderen te volgen en te begrijpen? Is betrokkene erg gevoelig voor bepaalde emoties bij anderen? Kleurt dit de vermeende intenties van anderen?\aKan betrokkene inzien dat anderen een andere visie op iets hebben? Hoe ervaart betrokkene een verschil van mening met anderen?\aKan betrokkene begrijpen en inschatten welke impact hij/zij op anderen heeft?"
                },
                "Intimiteit": {
                    "toelichting": "Is betrokkene in staat tot positieve verbondenheid met anderen? Is verbondenheid stabiel en langdurig positief?\aHeeft betrokkene een capaciteit to intieme/nabije verbondenheid? Is er sprake van wederkerigheid (i.e. wederzijdse waardering maar ook het vermogen om afhankelijkheid en kwetsbaarheid te verdragen)?\aIs betrokkene in staat tot constructieve samenwerking?"
                },
            },
        },
        "Bespreking": {
            "Beschrijvende diagnose": {
                "Context": {},
                "Door betrokkene ervaren en gerapporteerde klachten": {
                    "toelichting": "Bespreek hier zowel hetgeen betrokkene anamnestisch heeft vermeld als hetgeen uit de zelfrapportage-meetinstrumenten blijkt. Bespreek dit in aparte alinea's en geef weer of het anamnestische beeld wel/niet overeenkomt met het beel op de zelfrapportage-instrumenten"
                },
                "Geobserveerde symptomen": {
                    "toelichting": "Beschrijf hier de tijdens het onderzoek geobserveerde afwijkingen zoals die bijvoorbeeld blijken bij het psychiatrisch onderzoek. Bespreek hier ook eventueel heteroanamnestische informatie en objectieve informatie uit andere bronnen"
                },
                "Persoonlijkheidsfunctioneren": {
                    "toelichting": "Bespreek hier in ieder geval kort de wijze waarop betrokkene zichzelf in de paragraaf Persoonlijkheidsfunctioneren beschrijft. Bespreek hier ook hetgeen betrokkene over zichzelf zegt op de NPV-2-R en de NKPV\aBespreek hier ook de eigen bevindingen omtrent het persoonlijkheidsfunctioneren"
                },
                "Hypothese over de organisatie van de persoonlijkheid": {
                    "toelichting": "Ga hier uit van de DTP interpretatie van de NKPV en benoem die als dusdanig. Vermijd het als dusdanig benoemen van de profielen maar volsta met het benoemen van de verhouding tussen angstgevoeligheid/controle, de invloed van het temperament en de wijze waarop symptomatologie zich al dan niet uit. Ook aanvullende indrukken of hypotheses over de organisatie van de persoonlijkheid kunnen hier genoemd worden. Bespreek hier ook eventuel afwijkingen tussen hetgeen door betrokkene gezegd of anderszins gerapporteerd is enerzijds en hetgeen geobserveerd of objectief blijkt anderszins."
                },
                "Hypothese over beïnvloedende factoren in de huidige sociaal-maatschappelijke context": {},
                "Hypothese over somatische beïnvloedende factoren": {},
                "Hypothese over overige factoren van invloed": {
                    "toelichting": "Denk hier aan traumatisering, negatieve omstandigheden tijdens de opvoeding, hechtingsproblematiek etc."
                },
                "Hypothese over het toestandsbeeld": {},
            },
        },
    },
}


def get_report():
    reports = [
        [FML],
        [basis_rapport],
        [basis_rapport, basis_rapport_psychiatrie],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_interventieadvies,
            psychiatrie_interventieadvies_complex,
        ],
        [
            basis_rapport,
            basis_rapport_psychiatrie,
            psychiatrie_interventieadvies,
            psychiatrie_interventieadvies_kort,
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
