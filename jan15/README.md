# Oppgaver til øving i DAT2000 15. Januar 2024
## Oppsett
Vi skal bruke Apache Jena Fuseki, men vi er nødt til å kjøre den med Java, ikke fra Docker av tekniske årsaker..
Last ned denne [herifra](https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-4.10.0.zip)
Så pakker du ut apache jena fuseki til jan15-mappa.

Hvis du ikke har java så laster du ned dette, f.eks. fra https://learn.microsoft.com/en-gb/java/openjdk/download 

Naviger så til apache-jena-fuseki-4.10.0 mappa, og skriv:
```bash
java -jar fuseki-server.jar --file=../lecture.ttl /lecture
```

For å kunne utforske en graf visuelt så starter vi Graph Explorer (fra nytt terminalvindu)
```bash
 docker run --name graph_explorer --rm -p 8002:80 -e ENDPOINT_URL=http://localhost:3030/lecture/query -e LUCENE_SEARCH=no aksw/ontodia
 ```

Vi kan nå åpne Jena Fuseki ved å gå til http://localhost:3030/


## Oppgave 1:
0. Åpne Jena Fuseki og sjekk at du får kjørt default-spørringen. 
1. Søk etter Fido i Graph explorer, og se om du kan få opp alle ressursene vi har laget i en visualisering.
2. Søk etter Lucy i Graph explorer - hvorfor er det ingen resultater?
3. Gjør så alle ressursene det er snakk om har en rdfs:label. Vi må altså legge til f.eks. `ex:Lucy rdfs:label "Lucy" .`. Sjekk at det går an å søke nå. Du må restarte Jena men trenger ikke restarte graph explorer, bare trykk refresh. Pass opp for små skrivefeil.

### Oppgave 2:
Dette kan være et nyttig utgangspunkt for disse oppgavene.
Denne spørringen henter alle eiere og kjæledyrene deres.
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pets: <http://example.net/pets#>
PREFIX owl:<http://www.w3.org/2002/07/owl#> 
PREFIX ex:<http://example.net/instances#>

SELECT * WHERE {
  ?owner pets:hasPet ?pet .
} 
```
1. Sjekk at du får kjørt alle spørringene fra forelesningsnotatene. 
2. Skriv en spørring som henter alle kattene, og navnene deres
3. Skriv en spørring som henter navnet til alle hundene til noen som har en fisk, og navnet til denne personen, og navnet til fisken. 

## Oppgave 3:
Dette kan være et nyttig utgangspunkt for disse oppgavene.
Denne spørringen henter alle eiere og kjæledyrene deres.
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pets: <http://example.net/pets#>
PREFIX owl:<http://www.w3.org/2002/07/owl#> 
PREFIX ex:<http://example.net/instances#>

SELECT ?ownername WHERE {
  ?owner pets:hasPet ?pet .
  ?owner rdfs:label ?ownername .
  FILTER NOT EXISTS { ?pet rdfs:label "Fido" }
} 
```
1. Skriv en spørring som finner navnet på alle som ikke har en katt
2. Skriv en spørring som finner navnet på alle kjæledyrene til de som har en katt

Spørringen under er nyttig i neste oppgave.
Den henter ut alle som har kjæledyr og navnet deres hvis det finnes. 
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pets: <http://example.net/pets#>
PREFIX owl:<http://www.w3.org/2002/07/owl#> 
PREFIX ex:<http://example.net/instances#>

SELECT ?owner ?ownername WHERE {
  ?owner pets:hasPet ?pet .
  OPTIONAL {
    ?owner rdfs:label ?ownername .
  }
} 
```
3. Skriv en spørring som finner navnet til alle dyreeiere og navnet på alle kattene de har hvis de har katt.

## Oppgave 4. 
Som dere ser i Graph Explorer er det mulig å se på alle klassene, vi skal nå fikse dette.
1. Vi må si at alle klasser (`pets:Dog` etc.) er klasser. Legg til `pets:Dog a owl:Class .` etc. for alle disse. Sjekk at de dukker opp i classes i graph explorer.
2. Dette gir deg et flatt hierarki under `owl:Thing`. Legg til `pets:Dog rdfs:subClassOf pets:CuddlyPet .` osv. som du ønsker for å få litt system i sysakene. Minimum at katter og hunder er cuddly. Klassene burde også ha navn. Sjekk at du får til å navigere i hierarkiet. 
3. Lag en spørring som henter navnene til alle kjæledyr som er `pets:CuddlyPet`.


