## De Centrale Limietstelling

De Centrale Limietstelling (Engels: Central Limit Theorem of CLT) is zonder meer de meest belangrijke stelling in de statistiek en in data analyses. 


>De **Centrale Limietstelling** zegt dat als je $$n$$ onafhankelijk stochasten $$x_j$$ hebt, waarvan elke stochast zijn eigen verdeling heeft met gemiddelde  $$\mu_j$$ en variantie $$\sigma^2_j$$ (die niet persé dezelfde hoeven te zijn!), de som van deze stochasten $$\sum_j x_j$$ een normale verdeling zal volgen met het gemiddelde $$\sum_j \mu_j$$ en de variantie $$\sum_j \sigma^2_j$$. 

En als de som een normale verdeling volgt, dat geldt dat ook voor het gemiddelde! 

Wat deze stelling eigenlijk zegt is dat als je een combinatie hebt van vele oorzaken van onzekerheden, de uiteindelijke verdeling de normale verdeling zal hebben. En het maakt dus niet uit hoe de onderliggende verdelingen van de onzekerheden die je combineert eruit zien. Behalve dat ze een gedefinieerd gemiddelde en variantie moeten hebben. De Centrale Limietstelling verklaart waarom zoveel grootheden Normaal zijn verdeeld.
Meestal is er namelijk sprake van een combinatie van een grote hoeveelheid toevalligheden die een rol spelen bij de onzekerheid van een meting. Hetzelfde geldt vaak voor de eigenschappen van een populatie, de natuurlijke verdeling van deze eigenschappen zijn vaak ook Normaal verdeeld om dezelfde reden.

Denk maar eens aan de vorming van een zandkorrel of van een ster. Het is dan begrijpelijk dat de sterren in een bolhoop een Normale massa verdeling kennen. Of de grootte van de zandkorrel op een strand. 
Bij de vorming van een ster of zandkorrel zijn er ook vele toevalligheden die invloed hebben op de grootte van zo'n object.


Het bewijs van deze stelling is bijzonder ingewikkeld en zullen we hier niet behandelen. Eventueel kun je <a href="http://www.cs.toronto.edu/~yuvalf/CLT.pdf"> hier</a> verder lezen over de bewijsstelling.


Als je goed leest staat er dat de stochasten zelf een verdeling kennen met een gemiddelde $$\mu$$ en een variantie $$\sigma^2$$. Dat is een belangrijke voorwaarde. Wiskundig kun je laten zien dat bijvoorbeeld stochasten die volgens de Cauchy of Landau verdeeld zijn bij combinatie geen Normaal verdeling opleveren. Toch is die beperking niet heel groot. In de natuur zijn praktisch alle stochastische verdelingen beperkt en voldoen dus aan de Centrale Limietstelling.

**Twee leuke video's die de Centrale Limietstelling illustreren vindt kun je  <a href="https://www.youtube.com/watch?v=jvoxEYmQHNM">hier</a> en <a href="https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-mean/v/central-limit-theorem">hier</a> vinden.** 

De convergentie van de distributie naar de Normaal verdeling hangt af van de onderliggende stochastische verdelingen. 

<!--XX als het lukt nog een video maken-->