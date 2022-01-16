# Genetic-Algorithm-Knapsack
Når programmet køres, skal man indtaste størrelsen af populationen, samt antal generationer i terminalen. Herefter køres programmet, hvor den højeste værdi bliver printet i terminalen for hver løsning. Når programmet har kørt generationerne igennem, bliver løsningen(erne) printet ud som en liste af tuple. Disse tupler indeholder en liste af strings af de ting som er blevet pakket i tasken, samt værdien af løsningen.

For at ændre på mutations procenten, skal man ændre på variablet "mutationChance" (dette findes øverst i koden)
For at fjerne eller tilføje elementer til opgaven, skal man ændre på de to dictionaries i toppen (Jeg har ikke nået at lave en funktion til at ændre i det lettere)

For at installere de påkrævede moduler til at køre scriptet (selvfølgelig skal man navigere til fil placeringen inden):
`pip3 install -r requirements.txt`

For at køre programmet:
`python3 GA.py`
