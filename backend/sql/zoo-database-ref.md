# Zoo Database


## Reference

For reference, here's a list of all the tables in the zoo database:

### animals
This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.

 - name — the animal's name (example: 'George')
 - species — the animal's species (example: 'gorilla')
 - birthdate — the animal's date of birth (example: '1998-05-18')

### diet
This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one. If a species eats more than one food, there will be more than one row for that species.

 - species — the name of a species (example: 'hyena')
 - food — the name of a food that species eats (example: 'meat')

### taxonomy
This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.

 - name — the common name of the species (e.g. 'jackal')
 - species — the taxonomic species name (e.g. 'aureus')
 - genus — the taxonomic genus name (e.g. 'Canis')
 - family — the taxonomic family name (e.g. 'Canidae')
 - t_order — the taxonomic order name (e.g. 'Carnivora')

If you've never heard of this classification, don't worry about it; the details won't be necessary for this course. But if you're curious, Wikipedia articles [Taxonomy](http://en.wikipedia.org/wiki/Biological_classification) and (Biological classification)[http://en.wikipedia.org/wiki/Biological_classification] may help.

### ordernames

This table gives the common names for each of the taxonomic orders in the taxonomy table.

 - t_order — the taxonomic order name (e.g. 'Cetacea')
 - name — the common name (e.g. 'whales and dolphins')

## The SQL for it

And here are the SQL commands that were used to create those tables. We won't cover the create table command until lesson 4, but it may be interesting to look at:

```sql

create table animals (
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text);

create table ordernames (
       t_order text,
       name text);

```

## Data

`select * from animals`
```
+-------------+------------+------------+
|        name |    species |  birthdate |
+=============+============+============+
|      Andrea |     alpaca | 2001-01-16 |
|       Bruno |     alpaca | 2004-09-23 |
|     Charlie |     alpaca | 2004-09-23 |
|       Della |     alpaca | 2006-01-09 |
|        Emma |     alpaca | 2013-03-16 |
|        Fred | brown bear | 1993-05-02 |
|      George | brown bear | 1997-06-24 |
|       Molly | brown bear | 1981-10-17 |
|     Eliezer |      camel | 1971-03-08 |
|    Giuseppe |      camel | 1979-12-25 |
|        Taro |      camel | 1981-08-10 |
|        Fido |      dingo | 1999-08-04 |
|        Spot |      dingo | 2007-11-07 |
|       Rover |      dingo | 2008-08-24 |
|      Medusa |    echidna | 2003-01-31 |
| Zarathustra |     ferret | 2006-09-18 |
|    Zebediah |     ferret | 2006-10-11 |
|   Zephaniah |     ferret | 2010-02-02 |
|     Zenobia |     ferret | 2099-09-03 |
|        Zara |     ferret | 2007-12-17 |
|         Max |    gorilla | 2001-04-23 |
|        Dave |    gorilla | 1988-09-29 |
|       Becky |    gorilla | 1979-07-04 |
|         Liz |    gorilla | 1998-06-12 |
|      George |    gorilla | 2011-01-09 |
|      George |    gorilla | 1998-05-18 |
|     Wendell |    gorilla | 1982-09-24 |
|       Bjorn |    gorilla | 2000-03-07 |
|     Kristen |    gorilla | 1990-04-25 |
|    Cherries |      hyena | 2007-06-08 |
|        Biff |      hyena | 2011-06-09 |
|  Tinkerbell |      hyena | 2009-11-10 |
|      George |     iguana | 2013-10-18 |
|      Cheech |     iguana | 2006-12-19 |
|        Spot |     iguana | 2010-07-23 |
|      Andrea |     iguana | 1999-09-09 |
|       Devoe |     jackal | 2009-09-25 |
|       Duran |     jackal | 2009-09-20 |
|      Jethro |     jackal | 2012-04-29 |
|     Tiffany |     jackal | 2007-12-26 |
|         Sue |     jackal | 2003-12-21 |
|      Alison |      llama | 1997-11-24 |
|         Ben |      llama | 1984-01-05 |
|    Cordelia |      llama | 1990-10-21 |
|         Eli |      llama | 2002-02-22 |
|        John |      llama | 1986-01-17 |
|       Glenn |      llama | 1986-04-13 |
|         Meg |      llama | 2011-09-08 |
|         Mel |      llama | 2000-10-31 |
|    Veronica |      llama | 1994-07-09 |
|       Ricky |   mongoose | 2006-02-28 |
|     Charlie |      moose | 2001-12-19 |
|        Lucy |      moose | 1990-03-27 |
|       Patty |      moose | 1996-04-19 |
|   Woodstock |      moose | 2002-06-15 |
|     Francis |    narwhal | 1996-04-27 |
|       Bacon |    narwhal | 1975-02-07 |
|        Raja |  orangutan | 1975-04-09 |
|        Ratu |  orangutan | 1989-09-15 |
|      Putera |  orangutan | 1993-06-29 |
|       Gajah |  orangutan | 2011-05-26 |
|       Singa |  orangutan | 2012-11-03 |
|     Kambing |  orangutan | 1988-11-12 |
|       Chris |   platypus | 2003-12-21 |
|       Sandy |   platypus | 2008-09-09 |
|         Pat |   platypus | 2000-04-13 |
|        Mary |    raccoon | 2011-04-05 |
|      Martha |    raccoon | 2009-10-24 |
|        John |    raccoon | 2009-08-11 |
|         Mal |   sea lion | 1987-04-29 |
|         Zoe |   sea lion | 1991-05-19 |
|       River |   sea lion | 2004-07-08 |
|       Inara |   sea lion | 2001-08-18 |
|       Simon |   sea lion | 2000-12-16 |
|      Morgan |    unicorn | 1875-01-24 |
|      Laylah |    unicorn | 1752-05-20 |
|    Bertrand |    warthog | 2007-11-12 |
|     Hypatia |    warthog | 2007-05-20 |
|        Emmy |    warthog | 2008-04-15 |
|        Jack |        yak | 1996-09-20 |
|         Mac |        yak | 1996-10-19 |
|       Slack |        yak | 1997-09-05 |
|         Pac |        yak | 2000-08-09 |
|       Track |        yak | 2009-03-28 |
|       Owuru |      zebra | 1989-03-15 |
|     Ekwensu |      zebra | 1993-10-31 |
|       Imaha |      zebra | 1995-06-08 |
|      Adiaha |      zebra | 2005-05-12 |
|     Obi Ike |      zebra | 2014-04-30 |
+-------------+------------+------------+
```

`select * from taxonomy`

```
+------------+---------------+-----------------+-------------------+----------------+
|       name |       species |           genus |            family |        t_order |
+============+===============+=================+===================+================+
|     alpaca |         pacos |         Vicugna |         Camelidae |   Artiodactyla |
| brown bear |        arctos |           Ursus |           Ursidae |      Carnivora |
|      camel |   dromedarius |         Camelus |         Camelidae |   Artiodactyla |
|      dingo |         lupus |           Canis |           Canidae |      Carnivora |
|    echidna |     aculeatus |    Tachyglossus |    Tachyglossidae |    Monotremata |
|     ferret |      putorius |         Mustela |        Mustelidae |      Carnivora |
|    gorilla |       gorilla |         Gorilla |         Hominidae |       Primates |
|      hyena |       crocuta |         Crocuta |         Hyaenidae |      Carnivora |
|     iguana |        iguana |          Iguana |         Iguanidae |       Squamata |
|     jackal |        aureus |           Canis |           Canidae |      Carnivora |
|      llama |         glama |            Lama |         Camelidae |   Artiodactyla |
|      moose |         alces |           Alces |          Cervidae |   Artiodactyla |
|   mongoose |       parvula |        Helogale |       Herpestidae |      Carnivora |
|    narwhal |     monoceros |         Monodon |      Monodontidae |        Cetacea |
|  orangutan |        borneo |           Pongo |         Hominidae |       Primates |
|   platypus |      anatinus | Ornithorhynchus | Ornithorhynchidae |    Monotremata |
|    quetzal |       mocinno |    Pharomachrus |        Trogonidae |  Trogoniformes |
|    raccoon |         lotor |         Procyon |       Procyonidae |      Carnivora |
|   sea lion | californianus |        Zalophus |         Otariidae |      Carnivora |
|    unicorn |     monoceros |           Equus |           Equidae | Perissodactyla |
|    warthog |     africanus |    Phacochoerus |            Suidae |   Artiodactyla |
|        yak |     grunniens |             Bos |           Bovidae |   Artiodactyla |
|      zebra |        quagga |           Equus |           Equidae | Perissodactyla |
+------------+---------------+-----------------+-------------------+----------------+
```

`select * from ordernames`

```
+----------------+----------------------+
|        t_order |                 name |
+================+======================+
|   Artiodactyla |  even-toed ungulates |
|      Carnivora |           carnivores |
|    Monotremata |           monotremes |
|       Primates |             primates |
|       Squamata |   lizards and snakes |
|        Cetacea |  whales and dolphins |
|  Trogoniformes | trogons and quetzals |
| Perissodactyla |   odd-toed ungulates |
|     Chiroptera |                 bats |
+----------------+----------------------+
```

`select * from diet`

```
+------------+-----------+
|    species |      food |
+============+===========+
|     alpaca |    plants |
| brown bear |      fish |
| brown bear |      meat |
| brown bear |    plants |
|      camel |    plants |
|      dingo |      meat |
|    echidna |   insects |
|     ferret |      meat |
|     ferret |      eggs |
|    gorilla |    plants |
|      hyena |      meat |
|     iguana |    plants |
|     jackal |      meat |
|      llama |    plants |
|      moose |    plants |
|   mongoose |    snakes |
|   mongoose |      eggs |
|    narwhal |      fish |
|  orangutan |    plants |
|  orangutan |   insects |
|   platypus |   insects |
|   platypus | shellfish |
|    quetzal |   insects |
|    quetzal |    plants |
|    raccoon |   insects |
|    raccoon |    plants |
|    raccoon |      meat |
|    raccoon | shellfish |
|   sea lion |      fish |
|    unicorn |    plants |
|    warthog |    plants |
|    warthog |      meat |
|    warthog |   insects |
|        yak |    plants |
|      zebra |    plants |
+------------+-----------+
```

## Exercises

```sql

-- Write a query that returns all the species in the zoo, and how many
-- animals of each species there are, sorted with the most populous
-- species at the top.
--
-- The result should have two columns:  species and number.
--
-- The animals table has columns (name, species, birthdate) for each animal.

select species, count(*) as num
from animals
group by species
order by num desc

```

```sql
-- Insert a newborn baby opossum into the animals table and verify that it's
-- been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
-- 
-- SELECT_QUERY should find the names and birthdates of all opossums.
-- 
-- INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
-- (Or you can choose any other date you like.)
--
-- The animals table has columns (name, species, birthdate) for each individual.

select name, birthdate from animals where species = 'opossum';

insert into animals (name, species, birthdate) values ('Puff Daddy', 'opossum', '2010-02-23');
```


```sql
-- Find the names of the individual animals that eat fish.
--
-- The animals table has columns (name, species, birthdate) for each individual.
-- The diet table has columns (species, food) for each food that a species eats.

select animals.name from animals, diet where diet.species = animals.species and diet.food = 'fish'

```


```sql
-- Find the one food that is eaten by only one animal.
--
-- The animals table has columns (name, species, birthdate) for each
-- individual.
-- The diet table has columns (species, food) for each food that a
-- species eats.

select diet.food, count(*) as num
from animals, diet
where diet.species = animals.species
group by diet.food
having num = 1
```

```sql
-- List all the taxonomic orders, using their common names, sorted by the
-- number of animals of that order that the zoo has.
-- 
-- The animals table has (name, species, birthdate) for each individual.
-- The taxonomy table has (name, species, genus, family, t_order) for each species.
-- The ordernames table has (t_order, name) for each order.
-- 
-- Be careful:  Each of these tables has a column "name", but they don't
-- have the same meaning!  animals.name is an animal's individual name. 
-- taxonomy.name is a species' common name (like 'brown bear'). 
-- And ordernames.name is the common name of an order (like 'Carnivores').

select ordernames.name, count(*) as num
from animals
join taxonomy on taxonomy.name = animals.species
join ordernames on taxonomy.t_order = ordernames.t_order
group by ordernames.t_order
order by num desc

```