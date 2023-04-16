CREATE SCHEMA IF NOT EXISTS viewjs_db_schema;

GRANT ALL ON SCHEMA viewjs_db_schema to viewsjs;

CREATE TABLE IF NOT EXISTS viewjs_db_schema.common
(
    id        uuid UNIQUE NOT NULL,
    createdAt timestamp   NOT NULL,
    updatedAt timestamp,
    CONSTRAINT common_primary_key primary key (id)
    );
ALTER TABLE viewjs_db_schema.common
    OWNER TO viewsjs;
COMMENT ON TABLE viewjs_db_schema.common IS 'Common table from which all tables inherit';

CREATE TABLE IF NOT EXISTS viewjs_db_schema.organization
(
    CONSTRAINT organization_primary_key primary key (id)
    )
    INHERITS (viewjs_db_schema.common);
ALTER TABLE viewjs_db_schema.organization
    OWNER TO viewjs;
COMMENT ON TABLE viewjs_db_schema.organization IS 'organization table'

CREATE TABLE IF NOT EXISTS viewjs_db_schema.user
(
    organizationId uuid,
    CONSTRAINT user_primary_key primary key (id),
    CONSTRAINT user_organization_fkey foreign key (organizationId) REFERENCES viewjs_db_schema.organization (id)
    )
    INHERITS (viewjs_db_schema.common);
ALTER TABLE viewjs_db_schema.user
    OWNER TO viewjs;
COMMENT ON TABLE viewjs_db_schema.user IS 'user table'