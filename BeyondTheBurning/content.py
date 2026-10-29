# All of the written content for the site lives here, so the templates stay short.
#
# SOURCES  = the research library (every study the site cites)
# PAGES    = the topic pages (Understanding, Respiratory, Reproductive, etc.)
#
# Each section on a page can have an "evidence" label:
#   "established"  -> well-documented medical effect
#   "association"  -> studies found a link, but it is not proven to be the cause
#   "unknown"      -> not enough research to say

SURVEY_URL = "https://redcap.ahc.umn.edu/redcap/surveys/?s=N334D4N9J7T9YXE3"

EVIDENCE_LABELS = {
    "established": "Established effect",
    "association": "Observed association",
    "unknown": "Insufficient evidence",
}

SOURCES = {
    "cdc": {
        "title": "Riot Control Agents (Chemical Fact Sheet)",
        "authors": "U.S. Centers for Disease Control and Prevention",
        "year": "Current",
        "journal": "CDC Chemical Emergencies",
        "type": "Government public-health guidance",
        "sample": "Not applicable",
        "findings": "Describes symptoms by body part, long-term effects after prolonged or heavy "
                    "exposure (especially indoors), step-by-step decontamination, and treatment. "
                    "States that there is no antidote for riot control agent poisoning.",
        "limitations": "General guidance, not a research study.",
        "url": "https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/riot-control-agents.html",
    },
    "hassan2023": {
        "title": "More Than Tears: Associations Between Exposure to Chemical Agents Used by Law "
                 "Enforcement and Adverse Reproductive Health Outcomes",
        "authors": "Hassan A, Ojanen-Goldsmith A, Hing AK, Mahoney M, Traxler S, Boraas CM",
        "year": "2023",
        "journal": "Frontiers in Epidemiology",
        "type": "Cross-sectional observational study (University of Minnesota researchers)",
        "sample": "1,276 participants",
        "findings": "83% reported at least one reproductive health outcome: uterine cramping (69%), "
                    "early menstrual bleeding (55%), breast tenderness (30%), delayed menstrual "
                    "bleeding (21%). People exposed on 5 or more days had about 2.6 times the odds "
                    "of an adverse reproductive outcome.",
        "limitations": "Self-reported symptoms; participants were recruited through social media, "
                       "not randomly chosen; cannot prove cause and effect.",
        "url": "https://www.frontiersin.org/journals/epidemiology/articles/10.3389/fepid.2023.1177874/full",
    },
    "portland2021": {
        "title": "Health Issues and Healthcare Utilization Among Adults Who Reported Exposure to "
                 "Tear Gas During 2020 Portland (OR) Protests: A Cross-Sectional Survey",
        "authors": "Torgrimson-Ojerio BN, Mularski KS, Peyton MR, Keast EM, Hassan A, Ivlev I",
        "year": "2021",
        "journal": "BMC Public Health",
        "type": "Cross-sectional online survey",
        "sample": "2,257 adults (1,650 in the menstrual-health analysis)",
        "findings": "93.7% reported physical and 72.4% reported psychological health issues; "
                    "54.6% received or planned to seek medical or mental health care. 54.5% of "
                    "respondents who could menstruate reported menstrual changes. Health issues "
                    "increased with the number of days exposed.",
        "limitations": "Convenience sample of volunteers; self-reported, after-the-fact answers; "
                       "results may not apply to the whole population.",
        "url": "https://link.springer.com/article/10.1186/s12889-021-10859-w",
    },
    "arbak2014": {
        "title": "Long Term Effects of Tear Gases on Respiratory System: Analysis of 93 Cases",
        "authors": "Arbak P, Başer İ, Kumbasar ÖÖ, Ülger F, Kılıçaslan Z, Evyapan F",
        "year": "2014",
        "journal": "The Scientific World Journal",
        "type": "Cross-sectional comparison study",
        "sample": "93 frequently exposed men vs. 55 unexposed men",
        "findings": "Exposed men reported more shortness of breath (63.4% vs. 32.1%), chest "
                    "tightness (37.6% vs. 15.2%), daily winter phlegm, and morning cough, and had "
                    "lower mid-expiratory airflow. The authors concluded exposed people may be at "
                    "risk for chronic bronchitis.",
        "limitations": "Small, all-male sample; relied on memory of exposure; exposed smokers smoked "
                       "more cigarettes per day; the chronic bronchitis difference was not "
                       "statistically significant.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4132311/",
    },
    "dimitroglou2015": {
        "title": "Exposure to the Riot Control Agent CS and Potential Health Effects: "
                 "A Systematic Review of the Evidence",
        "authors": "Dimitroglou Y, Rachiotis G, Hadjichristodoulou C",
        "year": "2015",
        "journal": "International Journal of Environmental Research and Public Health",
        "type": "Systematic review",
        "sample": "35 studies",
        "findings": "CS mainly affects the skin, eyes, and lungs. Life-threatening and long-term "
                    "effects were linked mostly to exposure in enclosed spaces. Police, "
                    "demonstrators, bystanders, and healthcare workers may all be at risk.",
        "limitations": "Most evidence came from case reports, which are low-level evidence.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4344673/",
    },
    "rothenberg2016": {
        "title": "Tear Gas: An Epidemiological and Mechanistic Reassessment",
        "authors": "Rothenberg C, Achanta S, Svendsen ER, Jordt SE",
        "year": "2016",
        "journal": "Annals of the New York Academy of Sciences",
        "type": "Scientific review",
        "sample": "Not applicable",
        "findings": "Links tear gas to lung, skin, and eye injuries, with higher risk for people "
                    "with chronic illness. Explains that tear gas agents act on TRPA1 and pepper "
                    "spray acts on TRPV1, nerve receptors involved in pain, cough, and asthma.",
        "limitations": "Review article; notes that health research has lagged behind how much "
                       "these agents are used.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5096012/",
    },
    "haar2017": {
        "title": "Health Impacts of Chemical Irritants Used for Crowd Control: A Systematic Review "
                 "of the Injuries and Deaths Caused by Tear Gas and Pepper Spray",
        "authors": "Haar RJ, Iacopino V, Ranadive N, Weiser SD, Dandu M",
        "year": "2017",
        "journal": "BMC Public Health",
        "type": "Systematic review",
        "sample": "31 studies from 11 countries; 5,131 injured people",
        "findings": "Documented 2 deaths and 58 permanent disabilities. Concluded these agents can "
                    "cause severe injury and, rarely, death, especially in enclosed spaces or when "
                    "fired directly at people.",
        "limitations": "Includes injuries from projectiles (canisters, pepper balls), not just the "
                       "chemicals. Counts collected cases, so it cannot give a risk rate for "
                       "everyone exposed.",
        "url": "https://pubmed.ncbi.nlm.nih.gov/29052530/",
    },
    "brown2021": {
        "title": "Reevaluating Tear Gas Toxicity and Safety",
        "authors": "Brown JL, Lyons CE, Toddes C, Monko T, Tyshynsky R",
        "year": "2021",
        "journal": "Inhalation Toxicology",
        "type": "Literature review (University of Minnesota Medical School)",
        "sample": "Not applicable",
        "findings": "Safety limits for CS are based mainly on animal studies scaled to humans. "
                    "Studies claiming CS is safe for people with asthma or high blood pressure "
                    "were small, mostly male, and followed people for about a week at most. "
                    "Long-term effects are poorly studied.",
        "limitations": "Review of existing studies; highlights gaps rather than new data.",
        "url": "https://pubmed.ncbi.nlm.nih.gov/34511005/",
    },
}


PAGES = [
    {
        "slug": "understanding",
        "number": 2,
        "nav": "Understanding Tear Gas",
        "title": "Understanding Tear Gas",
        "subtitle": "What are chemical crowd-control agents, and how do they affect the body?",
        "sections": [
            {
                "heading": "What is tear gas?",
                "paragraphs": [
                    "\"Tear gas\" is a general term for chemicals that cause intense irritation "
                    "when they touch the eyes, skin, and airways. Doctors and the CDC call them "
                    "riot control agents or chemical irritants.",
                    "Despite the name, tear gas usually is not a true gas. Most agents are solid "
                    "chemicals spread through the air as fine particles or a mist (aerosol).",
                ],
            },
            {
                "heading": "Types of chemical irritants",
                "bullets": [
                    "CS (2-chlorobenzalmalononitrile): the most widely used tear gas. Causes fast "
                    "irritation of the eyes, nose, throat, and lungs.",
                    "CN (chloroacetophenone): an older agent. Can cause serious eye, skin, and "
                    "lung injuries after heavy exposure.",
                    "CR (dibenzoxazepine): a very strong irritant. There is less human research "
                    "on CR than on CS.",
                    "OC (oleoresin capsicum): the active ingredient in pepper spray and pepper "
                    "balls. It comes from hot peppers and is chemically different from CS, CN, "
                    "and CR, but causes similar symptoms.",
                ],
            },
            {
                "heading": "How these chemicals affect the body",
                "evidence": "established",
                "paragraphs": [
                    "These chemicals switch on pain-sensing nerve receptors. Tear gas agents like "
                    "CS mainly activate a receptor called TRPA1, while the capsaicin in pepper "
                    "spray activates TRPV1. These receptors are involved in pain, coughing, and "
                    "asthma, which is why exposure causes burning, tearing, and coughing.",
                    "With heavier exposure, the irritation can turn into inflammation, airway "
                    "spasms (bronchospasm), and tissue injury.",
                ],
                "sources": ["rothenberg2016"],
            },
            {
                "heading": "How exposure happens",
                "bullets": [
                    "Breathing in airborne particles",
                    "Direct contact with the eyes",
                    "Contact with exposed skin",
                    "Touching contaminated clothing, hair, or objects",
                ],
            },
            {
                "heading": "Why the conditions matter",
                "evidence": "established",
                "paragraphs": [
                    "Outdoors, exposure depends on wind, weather, and how much is released. In "
                    "enclosed spaces the chemical can build up, which raises the risk of serious "
                    "injury. The CDC says long-term effects are more likely after prolonged or "
                    "heavy exposure, especially indoors.",
                    "A short, low-level exposure is not the same as a long exposure in a closed "
                    "room. Risk depends on the chemical, the amount, the setting, and the "
                    "person's health.",
                ],
                "sources": ["cdc", "dimitroglou2015"],
            },
        ],
    },
    {
        "slug": "respiratory",
        "number": 3,
        "nav": "Respiratory Health",
        "title": "Respiratory and Pulmonary Health",
        "subtitle": "What happens when tear gas enters the lungs?",
        "sections": [
            {
                "heading": "Why the lungs are a main target",
                "paragraphs": [
                    "When airborne irritants are breathed in, they land on the moist lining of the "
                    "nose, throat, and airways. They trigger nerves that cause coughing, extra "
                    "mucus, and difficulty breathing.",
                ],
            },
            {
                "heading": "Immediate respiratory effects",
                "evidence": "established",
                "bullets": [
                    "Coughing and throat burning: a protective reflex to clear the irritant.",
                    "Chest tightness, wheezing, and shortness of breath.",
                    "Bronchospasm: the muscles around the airways squeeze and narrow them.",
                    "Asthma attacks: people with asthma can have their symptoms suddenly get worse.",
                ],
                "sources": ["cdc"],
            },
            {
                "heading": "Severe complications",
                "evidence": "established",
                "paragraphs": [
                    "Heavy or prolonged exposure can cause chemical pneumonitis (chemical "
                    "inflammation of the lungs) and pulmonary edema, where fluid builds up in the "
                    "lungs and blocks oxygen from getting into the blood. The CDC lists "
                    "respiratory failure and death as possible outcomes in severe cases.",
                    "These complications are much less common than short-term irritation, but they "
                    "can be life-threatening.",
                ],
                "sources": ["cdc", "dimitroglou2015"],
            },
            {
                "heading": "Research on long-term lung effects",
                "evidence": "association",
                "paragraphs": [
                    "A 2014 study compared 93 men who were frequently exposed to tear gas with 55 "
                    "men who were not. The exposed group reported much more shortness of breath "
                    "(63.4% vs. 32.1%) and chest tightness (37.6% vs. 15.2%), plus more daily "
                    "phlegm and morning cough in winter. They also had lower airflow in the "
                    "smaller airways on breathing tests.",
                    "The researchers concluded that frequently exposed people may be at risk for "
                    "chronic bronchitis. However, the study was small, all male, relied on memory "
                    "of past exposures, and the exposed smokers smoked more, which makes it hard "
                    "to prove tear gas was the cause.",
                ],
                "sources": ["arbak2014"],
            },
            {
                "heading": "Can tear gas cause chronic lung disease?",
                "evidence": "unknown",
                "paragraphs": [
                    "The CDC notes that heavy exposure can lead to long-lasting breathing problems "
                    "such as asthma. But researchers have not measured how often chronic lung "
                    "disease develops in the general public after exposure. Studies that follow "
                    "exposed people for years are still needed.",
                ],
                "sources": ["cdc", "brown2021"],
            },
            {
                "heading": "When to get medical help",
                "callout": True,
                "paragraphs": [
                    "Get emergency care for severe shortness of breath, wheezing that won't stop, "
                    "chest pain, confusion, fainting, or symptoms that get worse after leaving the "
                    "area. Breathing symptoms that last for days should also be checked by a doctor.",
                ],
            },
        ],
    },
    {
        "slug": "reproductive",
        "number": 4,
        "nav": "Reproductive Health",
        "title": "Reproductive Health and Pregnancy",
        "subtitle": "Can tear gas exposure affect the reproductive system?",
        "sections": [
            {
                "heading": "An understudied question",
                "paragraphs": [
                    "Most early safety research on tear gas focused on the eyes, skin, and lungs. "
                    "Reproductive health got very little attention until recent studies of people "
                    "exposed during protests found many reports of menstrual changes.",
                    "Menstrual cycles are controlled by signals between the brain, ovaries, and "
                    "hormones, and they can change because of stress, illness, medications, and "
                    "other factors. Researchers are studying whether chemical irritants add to this.",
                ],
            },
            {
                "heading": "The 2023 \"More Than Tears\" study",
                "evidence": "association",
                "paragraphs": [
                    "University of Minnesota researchers surveyed 1,276 people with a uterus who "
                    "reported exposure to chemical agents used by law enforcement. 83% reported "
                    "at least one reproductive health problem afterward.",
                ],
                "bullets": [
                    "Uterine cramping: 69%",
                    "Early menstrual bleeding: 55%",
                    "Breast tenderness: 30%",
                    "Delayed menstrual bleeding: 21%",
                ],
                "after": [
                    "People exposed on 5 or more days had about 2.6 times the odds of reporting "
                    "an adverse reproductive outcome, which suggests more exposure was linked to "
                    "more symptoms. This shows an association, not proof that the chemicals "
                    "caused the symptoms.",
                ],
                "sources": ["hassan2023"],
            },
            {
                "heading": "The 2021 Portland study",
                "evidence": "association",
                "paragraphs": [
                    "Researchers surveyed 2,257 adults exposed to tear gas during the 2020 "
                    "protests in Portland, Oregon. Of the 1,650 respondents who could menstruate, "
                    "54.5% reported menstrual changes. The most common were more cramping "
                    "(36.6%), unusual spotting (27.8%), heavier bleeding (23.6%), and more days "
                    "of bleeding (18.9%).",
                    "Like the 2023 study, this survey used volunteers and self-reported answers, "
                    "so it cannot prove tear gas directly caused these changes.",
                ],
                "sources": ["portland2021"],
            },
            {
                "heading": "Could tear gas affect hormones?",
                "evidence": "unknown",
                "paragraphs": [
                    "Researchers have suggested possible explanations, including inflammation, "
                    "physical stress on the body, and effects on hormone signaling. None of "
                    "these has been proven in humans, and the exact cause of the reported "
                    "menstrual changes is still unknown.",
                ],
            },
            {
                "heading": "Pregnancy, miscarriage, and fertility",
                "evidence": "unknown",
                "paragraphs": [
                    "Severe breathing problems during pregnancy can threaten the health of the "
                    "pregnant person. Some reports describe pregnancy losses after exposure, but "
                    "there is not enough evidence to know whether tear gas raises the risk of "
                    "miscarriage, birth defects, or infertility. The 2023 study included only a "
                    "small number of people who were pregnant when exposed, too few to estimate "
                    "risk.",
                ],
                "sources": ["hassan2023", "brown2021"],
            },
            {
                "heading": "What research is still needed",
                "bullets": [
                    "Hormone measurements before and after exposure",
                    "Menstrual changes tracked over time, not just remembered later",
                    "Measured exposure amounts and durations",
                    "Pregnancy outcomes in larger groups",
                    "Effects on fertility",
                    "Separating the effects of the chemicals from the effects of stress",
                ],
            },
            {
                "heading": "Key takeaway",
                "callout": True,
                "paragraphs": [
                    "Two studies found that many exposed people reported menstrual changes, and "
                    "more exposure was linked to more symptoms. These findings deserve more "
                    "research, but current evidence does not show that tear gas causes "
                    "infertility, miscarriage, or permanent reproductive damage.",
                ],
            },
        ],
    },
    {
        "slug": "long-term",
        "number": 5,
        "nav": "Long-Term Effects",
        "title": "Long-Term and Repeated Exposure",
        "subtitle": "What happens after the immediate symptoms go away?",
        "sections": [
            {
                "heading": "Short-term vs. long-term effects",
                "paragraphs": [
                    "According to the CDC, symptoms usually fade 15 to 30 minutes after a person "
                    "leaves the area and is cleaned off, and if symptoms clear up quickly, "
                    "long-term effects are unlikely. However, the Portland study found many people "
                    "reported health problems lasting several days.",
                ],
                "sources": ["cdc", "portland2021"],
            },
            {
                "heading": "Documented long-lasting effects",
                "evidence": "established",
                "bullets": [
                    "Eyes: glaucoma, scarring, and cataracts after heavy exposure; blindness in "
                    "severe cases",
                    "Lungs: ongoing breathing problems such as asthma",
                    "Skin: chemical burns and dermatitis (skin inflammation)",
                ],
                "after": [
                    "The CDC says these are more likely after prolonged or heavy exposure, "
                    "especially indoors. Not everyone exposed develops them.",
                ],
                "sources": ["cdc", "dimitroglou2015"],
            },
            {
                "heading": "Repeated exposure",
                "evidence": "association",
                "paragraphs": [
                    "Repeated exposure means being exposed many times over days, weeks, or months. "
                    "Both the 2021 Portland and 2023 \"More Than Tears\" studies found that people "
                    "exposed on more days reported more health problems, a pattern called a "
                    "dose-response. The 2014 respiratory study also found more breathing "
                    "complaints among frequently exposed men.",
                ],
                "sources": ["portland2021", "hassan2023", "arbak2014"],
            },
            {
                "heading": "Severe and permanent injuries",
                "evidence": "established",
                "paragraphs": [
                    "A 2017 review of 31 studies from 11 countries covered 5,131 injured people. "
                    "It documented 2 deaths and 58 permanent disabilities.",
                    "Some of these injuries came from the projectiles used to deliver the "
                    "chemicals (like canisters and pepper balls), not just the chemicals "
                    "themselves. Because the review collected injury cases, its numbers show that "
                    "serious harm can happen but cannot tell us the risk for every exposed person.",
                ],
                "sources": ["haar2017"],
            },
            {
                "heading": "What makes exposure worse",
                "bullets": [
                    "Higher concentration of the chemical",
                    "Longer exposure time",
                    "More frequent exposure",
                    "Enclosed spaces with poor airflow",
                    "Existing lung or heart conditions",
                    "Heat and humidity",
                ],
                "sources": ["haar2017", "cdc"],
            },
            {
                "heading": "What we still don't know",
                "evidence": "unknown",
                "paragraphs": [
                    "Most tear gas research is case reports, surveys, or small studies. Safety "
                    "limits for CS are based mainly on animal studies, and the studies claiming it "
                    "is safe for people with asthma or high blood pressure followed small groups "
                    "of mostly men for about a week. Very few studies follow large groups of "
                    "civilians over several years.",
                    "Scientists still need to find out whether repeated exposure raises the "
                    "long-term risk of chronic lung disease, reproductive problems, or other "
                    "health conditions.",
                ],
                "sources": ["brown2021", "dimitroglou2015"],
            },
            {
                "heading": "Why long-term studies matter",
                "callout": True,
                "paragraphs": [
                    "Longitudinal studies follow the same people over time. With lung function "
                    "tests, medical exams, measured exposures, and a comparison group, they can "
                    "show whether exposure comes before illness, which surveys alone cannot do.",
                ],
            },
        ],
    },
    {
        "slug": "vulnerable",
        "number": 6,
        "nav": "Vulnerable Populations",
        "title": "Vulnerable Populations and Community Exposure",
        "subtitle": "Why exposure does not affect everyone the same way.",
        "sections": [
            {
                "heading": "Who is at higher risk?",
                "evidence": "established",
                "paragraphs": [
                    "Reviews of the research agree that people with chronic illnesses are at "
                    "higher risk of harm from tear gas. Age, existing health conditions, and "
                    "exposure conditions all change how a person is affected.",
                ],
                "sources": ["rothenberg2016"],
            },
            {
                "heading": "Children and infants",
                "evidence": "unknown",
                "paragraphs": [
                    "Children's lungs are still developing and they breathe faster than adults, "
                    "so they may take in more of an irritant for their size. Research focused on "
                    "children and tear gas is very limited, so long-term effects are unknown.",
                ],
            },
            {
                "heading": "Pregnant people",
                "evidence": "unknown",
                "paragraphs": [
                    "Pregnancy changes breathing, circulation, and oxygen needs. Severe "
                    "breathing problems during pregnancy need urgent medical care. The direct "
                    "effects of tear gas on a developing pregnancy have not been well studied "
                    "in humans.",
                ],
                "sources": ["hassan2023"],
            },
            {
                "heading": "People with asthma, COPD, or other lung disease",
                "evidence": "established",
                "paragraphs": [
                    "Chemical irritants can trigger airway narrowing and inflammation, which can "
                    "cause serious breathing trouble in people who already have lung disease. "
                    "Studies claiming CS is safe for people with asthma were small and short.",
                ],
                "sources": ["cdc", "brown2021"],
            },
            {
                "heading": "Older adults and people with heart conditions",
                "paragraphs": [
                    "Older adults may have less lung capacity and more heart or lung disease. "
                    "In early CS studies, people with high blood pressure had larger and "
                    "longer-lasting blood pressure increases after exposure.",
                ],
                "sources": ["brown2021"],
            },
            {
                "heading": "Bystanders and nearby residents",
                "evidence": "established",
                "paragraphs": [
                    "Once released, tear gas drifts. It can reach people who are not part of a "
                    "crowd: residents, workers, people walking by, and people inside nearby "
                    "buildings. A 2015 review found that bystanders and healthcare workers, not "
                    "just demonstrators and police, can be affected.",
                ],
                "sources": ["dimitroglou2015"],
            },
            {
                "heading": "Healthcare workers and secondary exposure",
                "paragraphs": [
                    "Chemicals on clothing and skin can expose the people helping someone who "
                    "was gassed. Proper decontamination, like bagging contaminated clothes, "
                    "lowers this risk.",
                ],
                "sources": ["dimitroglou2015", "cdc"],
            },
        ],
    },
    {
        "slug": "medical-care",
        "number": 7,
        "nav": "Medical Care",
        "title": "Medical Response and Exposure Care",
        "subtitle": "What to do after exposure, based on CDC guidance.",
        "sections": [
            {
                "heading": "Step 1: Get to fresh air",
                "paragraphs": [
                    "Leave the area as quickly and safely as possible. Outdoors, move upwind and "
                    "to higher ground, since the chemical can collect in low areas. If the "
                    "exposure happened inside a building, get out of the building.",
                ],
            },
            {
                "heading": "Step 2: Remove contaminated clothing",
                "paragraphs": [
                    "Chemicals stay on clothing. Cut clothes off instead of pulling them over "
                    "your head, so the chemical doesn't touch your face again.",
                ],
            },
            {
                "heading": "Step 3: Wash your skin",
                "paragraphs": [
                    "Wash exposed skin with soap and water. Don't scrub hard, and don't use "
                    "household chemicals or home remedies to \"neutralize\" it.",
                ],
            },
            {
                "heading": "Step 4: Rinse your eyes",
                "paragraphs": [
                    "If your eyes burn or your vision is blurry, rinse them with plain water "
                    "for 10 to 15 minutes. Take out contact lenses and don't put them back in. "
                    "Glasses can be washed with soap and water and worn again.",
                ],
            },
            {
                "heading": "Step 5: Bag contaminated items",
                "paragraphs": [
                    "Put contaminated clothing and contacts in a plastic bag, using gloves if "
                    "you can. Seal it, put it inside a second bag, and give it to emergency "
                    "responders.",
                ],
            },
            {
                "heading": "Step 6: Get medical care",
                "callout": True,
                "paragraphs": [
                    "Call 911 for trouble breathing, chest pain, confusion, fainting, serious eye "
                    "injuries, or chemical burns. For questions, you can call the Poison Help "
                    "Line at 1-800-222-1222.",
                ],
            },
            {
                "heading": "Is there an antidote?",
                "evidence": "established",
                "paragraphs": [
                    "No. The CDC states that there is no antidote for riot control agents. "
                    "Doctors treat the symptoms: giving oxygen, using asthma medicines like "
                    "bronchodilators and steroids to open the airways, rinsing the eyes until "
                    "no chemical remains, and using standard burn care for the skin.",
                ],
            },
            {
                "heading": "If symptoms don't go away",
                "paragraphs": [
                    "See a doctor for breathing problems, eye irritation, or other changes that "
                    "last. Tell them what chemical you may have been exposed to, where, for how "
                    "long, and what symptoms you've had.",
                ],
            },
        ],
        "page_sources": ["cdc"],
    },
]


def get_page(slug):
    """Return the topic page with this slug, or None."""
    for page in PAGES:
        if page["slug"] == slug:
            return page
    return None
