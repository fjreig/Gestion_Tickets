-- Auxiliar Function Prefix
CREATE OR REPLACE FUNCTION add_prefix(INTEGER) RETURNS text AS
    $$ select 'TK-'||to_char($1, 'FM0000000'); $$
    LANGUAGE sql immutable;


-- create the table tickets
CREATE TABLE IF NOT EXISTS public.tickets
(
    id serial,
	fechacreacion timestamp,
 	fechamodificacion timestamp,
	id_ticket TEXT UNIQUE NOT NULL GENERATED ALWAYS AS (add_prefix(id)) STORED,
    titulo varchar,
    descripcion varchar,
    estado varchar,
    step int,
    departmento varchar,
    PRIMARY KEY (id)
);

-- Data

INSERT INTO public.tickets (fechacreacion,fechamodificacion,titulo,descripcion,estado,step,departmento) VALUES
	 ('2025-01-09 16:52:43','2025-01-09 16:52:43','Cloud Storage Access Error','Unable to access cloud storage with persistent authorization errors. Multiple users affected across marketing department','Alta',4,'IT Support'),
	 ('2025-01-09 16:52:43','2025-01-09 16:52:43','Office Equipment Setup','Unable to access cloud storage with persistent authorization errors. Multiple users affected across marketing department','Media',2,'IT Support');