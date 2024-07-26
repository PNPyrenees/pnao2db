/* 
 * REMPLACER <ZSMTamponTable> et <ZSMCoeurTable> 
 * PAR LE NOM DE LA TABLE CORRESPONDANT 
 * (sous la forme "schema.nomTable") 
 */ 

/******************/ 
/* ZSMTamponTable */ 
CREATE TABLE <ZSMTamponTable>
(
    id_zsm_tampon integer primary key,
    code_zsm varchar(255),
    idcode_aire integer,
    code_aire varchar(255),
    nom_aire varchar(255),
    actif integer,
    aire_historique integer,
    idespece integer,
    cd_nom integer,
    espece varchar(255),
    nom_latin varchar(255),
    code_dep varchar(3),
    idsite integer,
    site varchar(255),
    equivalence_code_reseau varchar(255),
    geom geometry(Polygon, 2154)
);

/******************/ 
/* ZSMCoeurTable */ 
CREATE TABLE <ZSMCoeurTable>
(
    id_zsm_coeur integer primary key,
    code_zsm varchar(255),
    idcode_aire integer,
    code_aire varchar(255),
    nom_aire varchar(255),
    actif integer,
    aire_historique integer,
    idespece integer,
    cd_nom integer,
    espece varchar(255),
    nom_latin varchar(255),
    code_dep varchar(3),
    idsite integer,
    site varchar(255),
    equivalence_code_reseau varchar(255),
    info_rap varchar(255),
    geom geometry(Polygon, 2154)
);