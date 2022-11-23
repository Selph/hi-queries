# hi-queries

Verkefnið sem unnið var fyrir áfangan Inngangur að Máltækni - TÖL029M við Háskóla Íslands haustið 2023.

Notast var við `Flask` til að gera vefviðmót og `Railway.app` til að hýsa og er það hýst hér: https://hi-queries-production.up.railway.app/

## Tæki og tól

`Flask` til að búa til viðmót

`Railway.app` til hýsingar

`spacy`, `re` til að tóka

`islenska` til að gera íslenskar lemmanir, frá BÍN

`pandas` til að vinna með csv gögn

`numpy` til að vinna með fylki


## Hvað getur appið gert?

Appið tekur við spurningum frá notanda og skilar svörum. Appið getur svarað spurningum sem snúa að:

- Staðsetningum háskólabygginga
- Opnunartímum háskólabygginga
- Tímasetningu lokaprófa
- Hámu
- Nemendaþjónustum sviða
- Stúdentaráði HÍ
- Tölvuver UTS
- Náms- og Starfsráðgjöf HÍ
- Stjórn Nörd
- Vefmiðlum Nörd (facebook, discord, instagram)

## Hvernig vinnur appið?

# Server layer

- appið opnar server sem getur tekið við og skilað requests

# App layer

- appið tekur inn streng frá notanda
- appið býr til html útfrá gögnunum sem koma til baka úr logic layer

# Prepare layer

- appið tókar strenginn frá notanda
- appið fjarlægir óþarfa hluti eins og spurningarmerki og slíkt
- appið lemmar tókanirnar á íslensku með tóli frá BÍN

# Logic layer

- appið sigtar lykilorð úr spurningunni
- appið mátar lykilorðin við undirbúin csv gögn og mátar viðeigandi gögn
- appið skilar dict af gögnum sem eru viðeigandi svar við spurningunni
-  *ef verkefnið krefst ekki að mátað sé lykilorð við gögnin kemur staðlað svar frá appinu

## Dæmi um spurningar

- Hvenær opnar Gróska?
- Hvar er Háskólatorg?
- Hvar er háma/hvenær opnar háma?
- Hvenær er próf í TÖL105G?
- Hvar get ég fengið/fundið námsráðgjöf/starfsráðgjöf/sálfræðing í HÍ?
- Hvar eru tölvuverin?
- Hvar hef ég samband við nemendaþjónustu VoN/Félagsvísíndasviðs/etc ?
- Hvar er Stúdentaráð til húsa / hvað er símanúmerið/netfangið hjá stúdentaráði?
- Hver er ritari Nörd?
- Hvað er linkurinn á Discord server Nörd?
- Hverjir eru miðlar nörd yfir höfuð?
