from utils.pg import get_conn


def create_tables():
    create_onisep_programs_table()
    create_onisep_schools_table()
    create_parcoursup_programs_table()

def create_onisep_programs_table():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RAW_ONISEP_PROGRAMS (
            id TEXT PRIMARY KEY,
            inserted_at TIMESTAMP,
            action_de_formation_af_identifiant_onisep TEXT,
            formation_for_libelle TEXT,
            for_url_et_id_onisep TEXT,
            for_indexation_domaine_web_onisep TEXT,
            for_type TEXT,
            for_nature_du_certificat TEXT,
            for_url_referentiel TEXT,
            for_niveau_de_sortie TEXT,
            lieu_denseignement_ens_libelle TEXT,
            ens_url_et_id_onisep TEXT,
            ens_code_uai TEXT,
            ens_statut TEXT,
            ens_adresse TEXT,
            ens_code_postal TEXT,
            ens_commune TEXT,
            ens_departement TEXT,
            ens_academie TEXT,
            ens_region TEXT,
            ens_latitude FLOAT,
            ens_longitude FLOAT,
            ens_n_telephone TEXT,
            ens_site_web TEXT,
            ens_hebergement TEXT,
            ens_accessibilite TEXT,
            af_duree_cycle_standard TEXT,
            af_modalites_scolarite TEXT,
            af_elements_denseignement TEXT,
            af_cout_scolarite TEXT,
            af_cout_dinscription TEXT,
            af_modalites_accueil TEXT,
            af_page_web TEXT,
            af_date_de_modification TIMESTAMP,
            _geoloc TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def create_onisep_schools_table():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RAW_ONISEP_SCHOOLS (
            id TEXT PRIMARY KEY,
            inserted_at TIMESTAMP,
            code_uai TEXT,
            n_siret TEXT,
            type_detablissement TEXT,
            nom TEXT,
            sigle TEXT,
            statut TEXT,
            tutelle TEXT,
            universite_de_rattachement_libelle TEXT,
            universite_de_rattachement_id_et_url_onisep TEXT,
            etablissements_lies_libelles TEXT,
            etablissements_lies_url_et_id_onisep TEXT,
            boite_postale TEXT,
            adresse TEXT,
            cp TEXT,
            commune TEXT,
            commune_cog TEXT,
            cedex TEXT,
            telephone TEXT,
            arrondissement TEXT,
            departement TEXT,
            academie TEXT,
            region TEXT,
            region_cog TEXT,
            longitude_x FLOAT,
            latitude_y FLOAT,
            journees_portes_ouvertes TEXT,
            label_generation_2024 TEXT,
            url_et_id_onisep TEXT,
            _geoloc TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_parcoursup_programs_table():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RAW_PARCOURSUP_PROGRAMS (
            session TEXT,
            identifiant_de_létablissement TEXT,
            nom_de_létablissement TEXT,
            types_détablissement TEXT,
            types_de_formation TEXT,
            nom_long_de_la_formation TEXT,
            mentionsspécialités TEXT,
            formations_en_apprentissage TEXT,
            internat TEXT,
            aménagement TEXT,
            informations_complémentaires TEXT,
            région TEXT,
            département TEXT,
            commune TEXT,
            lien_vers_la_fiche_formation TEXT,
            lien_vers_les_données_statistiques_pour_lannée_antérieure TEXT,
            site_internet_de_létablissement TEXT,
            localisation TEXT,
            nom_court_de_la_formation TEXT,
            code_interne_parcoursup_de_la_formation TEXT,
            code_interne_parcoursup_pour_les_portails TEXT,
            etablissement_id_paysage TEXT,
            composante_id_paysage TEXT,
            rnd TEXT,
            code_formation TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
