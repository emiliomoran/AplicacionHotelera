--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

-- Started on 2019-09-08 09:52:12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE hotel;
--
-- TOC entry 2204 (class 1262 OID 33829)
-- Name: hotel; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE hotel WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Spain.1252' LC_CTYPE = 'Spanish_Spain.1252';


ALTER DATABASE hotel OWNER TO postgres;

\connect hotel

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12355)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 184 (class 1259 OID 50377)
-- Name: accesos_cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accesos_cliente (
    id integer NOT NULL,
    last_login timestamp with time zone,
    nombres character varying(100) NOT NULL,
    apellidos character varying(100) NOT NULL,
    fecha_nacimiento date,
    username character varying(100),
    email character varying(254) NOT NULL,
    password text NOT NULL,
    estado boolean NOT NULL,
    fecha_creacion timestamp with time zone NOT NULL,
    fecha_modificacion timestamp with time zone NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL
);


ALTER TABLE public.accesos_cliente OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 50375)
-- Name: accesos_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.accesos_cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accesos_cliente_id_seq OWNER TO postgres;

--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 183
-- Name: accesos_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.accesos_cliente_id_seq OWNED BY public.accesos_cliente.id;


--
-- TOC entry 186 (class 1259 OID 50392)
-- Name: accesos_perfil; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accesos_perfil (
    id integer NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.accesos_perfil OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 50390)
-- Name: accesos_perfil_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.accesos_perfil_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accesos_perfil_id_seq OWNER TO postgres;

--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 185
-- Name: accesos_perfil_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.accesos_perfil_id_seq OWNED BY public.accesos_perfil.id;


--
-- TOC entry 182 (class 1259 OID 50366)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 50364)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 196 (class 1259 OID 50444)
-- Name: reservas_booking; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservas_booking (
    id integer NOT NULL,
    booking_date timestamp with time zone NOT NULL,
    check_in_date timestamp with time zone NOT NULL,
    check_out_date timestamp with time zone NOT NULL,
    no_nights integer NOT NULL,
    is_removed boolean NOT NULL,
    create_date timestamp with time zone NOT NULL,
    update_date timestamp with time zone NOT NULL,
    bookingtype_id_id integer NOT NULL,
    customer_id_id integer NOT NULL,
    room_id_id integer NOT NULL,
    state_id_id integer NOT NULL
);


ALTER TABLE public.reservas_booking OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 50442)
-- Name: reservas_booking_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservas_booking_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservas_booking_id_seq OWNER TO postgres;

--
-- TOC entry 2211 (class 0 OID 0)
-- Dependencies: 195
-- Name: reservas_booking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservas_booking_id_seq OWNED BY public.reservas_booking.id;


--
-- TOC entry 188 (class 1259 OID 50409)
-- Name: reservas_bookingstate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservas_bookingstate (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(150) NOT NULL,
    is_removed boolean NOT NULL,
    create_date timestamp with time zone NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.reservas_bookingstate OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 50407)
-- Name: reservas_bookingstate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservas_bookingstate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservas_bookingstate_id_seq OWNER TO postgres;

--
-- TOC entry 2212 (class 0 OID 0)
-- Dependencies: 187
-- Name: reservas_bookingstate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservas_bookingstate_id_seq OWNED BY public.reservas_bookingstate.id;


--
-- TOC entry 190 (class 1259 OID 50417)
-- Name: reservas_bookingtype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservas_bookingtype (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(150) NOT NULL,
    is_removed boolean NOT NULL,
    create_date timestamp with time zone NOT NULL,
    update_date timestamp with time zone NOT NULL
);


ALTER TABLE public.reservas_bookingtype OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 50415)
-- Name: reservas_bookingtype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservas_bookingtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservas_bookingtype_id_seq OWNER TO postgres;

--
-- TOC entry 2213 (class 0 OID 0)
-- Dependencies: 189
-- Name: reservas_bookingtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservas_bookingtype_id_seq OWNED BY public.reservas_bookingtype.id;


--
-- TOC entry 194 (class 1259 OID 50433)
-- Name: reservas_room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservas_room (
    id integer NOT NULL,
    descripcion character varying(200) NOT NULL,
    path_image text,
    calificacion integer NOT NULL,
    num_camas integer NOT NULL,
    num_adultos integer NOT NULL,
    num_ninos integer NOT NULL,
    precio double precision NOT NULL,
    disponible boolean NOT NULL,
    eliminado boolean NOT NULL,
    fecha_creacion timestamp with time zone NOT NULL,
    fecha_modificacion timestamp with time zone NOT NULL,
    id_roomtype_id integer NOT NULL
);


ALTER TABLE public.reservas_room OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 50431)
-- Name: reservas_room_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservas_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservas_room_id_seq OWNER TO postgres;

--
-- TOC entry 2214 (class 0 OID 0)
-- Dependencies: 193
-- Name: reservas_room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservas_room_id_seq OWNED BY public.reservas_room.id;


--
-- TOC entry 192 (class 1259 OID 50425)
-- Name: reservas_roomtype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservas_roomtype (
    id integer NOT NULL,
    nombre character varying(150) NOT NULL,
    descripcion character varying(200) NOT NULL,
    eliminado boolean NOT NULL,
    fecha_creacion timestamp with time zone NOT NULL,
    fecha_modificacion timestamp with time zone NOT NULL
);


ALTER TABLE public.reservas_roomtype OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 50423)
-- Name: reservas_roomtype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservas_roomtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservas_roomtype_id_seq OWNER TO postgres;

--
-- TOC entry 2215 (class 0 OID 0)
-- Dependencies: 191
-- Name: reservas_roomtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservas_roomtype_id_seq OWNED BY public.reservas_roomtype.id;


--
-- TOC entry 2027 (class 2604 OID 50380)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_cliente ALTER COLUMN id SET DEFAULT nextval('public.accesos_cliente_id_seq'::regclass);


--
-- TOC entry 2028 (class 2604 OID 50395)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_perfil ALTER COLUMN id SET DEFAULT nextval('public.accesos_perfil_id_seq'::regclass);


--
-- TOC entry 2026 (class 2604 OID 50369)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 2033 (class 2604 OID 50447)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking ALTER COLUMN id SET DEFAULT nextval('public.reservas_booking_id_seq'::regclass);


--
-- TOC entry 2029 (class 2604 OID 50412)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_bookingstate ALTER COLUMN id SET DEFAULT nextval('public.reservas_bookingstate_id_seq'::regclass);


--
-- TOC entry 2030 (class 2604 OID 50420)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_bookingtype ALTER COLUMN id SET DEFAULT nextval('public.reservas_bookingtype_id_seq'::regclass);


--
-- TOC entry 2032 (class 2604 OID 50436)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_room ALTER COLUMN id SET DEFAULT nextval('public.reservas_room_id_seq'::regclass);


--
-- TOC entry 2031 (class 2604 OID 50428)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_roomtype ALTER COLUMN id SET DEFAULT nextval('public.reservas_roomtype_id_seq'::regclass);


--
-- TOC entry 2186 (class 0 OID 50377)
-- Dependencies: 184
-- Data for Name: accesos_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accesos_cliente (id, last_login, nombres, apellidos, fecha_nacimiento, username, email, password, estado, fecha_creacion, fecha_modificacion, is_staff, is_superuser) FROM stdin;
1	\N	emilio	morán pilligua	2019-09-06	\N	emiliojmp9@gmail.com	pbkdf2_sha256$150000$BEdO3YK8SQCn$Ph3RXbimSg2Vpcc2ZafNKAbESahtZK7tKuRuZ76PqFo=	t	2019-09-07 19:51:22.586014-05	2019-09-07 19:51:22.586014-05	f	f
\.


--
-- TOC entry 2216 (class 0 OID 0)
-- Dependencies: 183
-- Name: accesos_cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.accesos_cliente_id_seq', 1, true);


--
-- TOC entry 2188 (class 0 OID 50392)
-- Dependencies: 186
-- Data for Name: accesos_perfil; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accesos_perfil (id, usuario_id) FROM stdin;
1	1
\.


--
-- TOC entry 2217 (class 0 OID 0)
-- Dependencies: 185
-- Name: accesos_perfil_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.accesos_perfil_id_seq', 1, true);


--
-- TOC entry 2184 (class 0 OID 50366)
-- Dependencies: 182
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	accesos	0001_initial	2019-09-07 14:19:01.153377-05
2	reservas	0001_initial	2019-09-07 14:19:11.168294-05
3	reservas	0002_auto_20190907_2130	2019-09-07 21:30:40.833489-05
4	reservas	0003_auto_20190907_2131	2019-09-07 21:31:24.227013-05
5	reservas	0004_auto_20190907_2134	2019-09-07 21:34:34.970624-05
\.


--
-- TOC entry 2218 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 5, true);


--
-- TOC entry 2198 (class 0 OID 50444)
-- Dependencies: 196
-- Data for Name: reservas_booking; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_booking (id, booking_date, check_in_date, check_out_date, no_nights, is_removed, create_date, update_date, bookingtype_id_id, customer_id_id, room_id_id, state_id_id) FROM stdin;
32	2019-09-08 09:00:21.69401-05	2019-09-05 23:34:39.554642-05	2019-09-07 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	11	1
37	2019-09-08 09:00:21.69401-05	2019-09-01 21:34:39.554642-05	2019-09-03 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	12	1
43	2019-09-08 09:00:21.69401-05	2019-09-06 21:34:39.554642-05	2019-09-07 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	19	1
44	2019-09-08 09:00:21.69401-05	2019-09-07 21:34:39.554642-05	2019-09-07 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	18	1
45	2019-09-08 09:00:21.69401-05	2019-09-07 21:34:39.554642-05	2019-09-07 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	16	1
33	2019-09-08 09:00:21.69401-05	2019-09-08 21:34:39.554642-05	2019-09-10 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	12	2
34	2019-09-08 09:00:21.69401-05	2019-09-08 21:34:39.554642-05	2019-09-10 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	13	2
35	2019-09-08 09:00:21.69401-05	2019-09-09 21:34:39.554642-05	2019-09-10 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	14	3
36	2019-09-08 09:00:21.69401-05	2019-09-08 21:34:39.554642-05	2019-09-10 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	11	2
38	2019-09-08 09:00:21.69401-05	2019-09-10 21:34:39.554642-05	2019-09-14 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	15	3
39	2019-09-08 09:00:21.69401-05	2019-09-15 21:34:39.554642-05	2019-09-16 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	20	3
40	2019-09-08 09:00:21.69401-05	2019-09-08 21:34:39.554642-05	2019-09-11 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	19	2
41	2019-09-08 09:00:21.69401-05	2019-09-12 21:34:39.554642-05	2019-09-14 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	11	3
42	2019-09-08 09:00:21.69401-05	2019-09-20 21:34:39.554642-05	2019-09-21 21:34:39.554642-05	2	f	2019-09-08 09:00:21.69401-05	2019-09-08 09:00:21.69401-05	4	1	13	3
\.


--
-- TOC entry 2219 (class 0 OID 0)
-- Dependencies: 195
-- Name: reservas_booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_booking_id_seq', 45, true);


--
-- TOC entry 2190 (class 0 OID 50409)
-- Dependencies: 188
-- Data for Name: reservas_bookingstate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_bookingstate (id, name, description, is_removed, create_date, update_date) FROM stdin;
1	Pasada	Reserva pasada	f	2019-09-07 19:21:45.235769-05	2019-09-07 19:21:45.235769-05
2	Actual	Reserva actual	f	2019-09-07 19:21:45.235769-05	2019-09-07 19:21:45.235769-05
3	Futura	Reserva futura	f	2019-09-07 19:21:45.235769-05	2019-09-07 19:21:45.235769-05
\.


--
-- TOC entry 2220 (class 0 OID 0)
-- Dependencies: 187
-- Name: reservas_bookingstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_bookingstate_id_seq', 3, true);


--
-- TOC entry 2192 (class 0 OID 50417)
-- Dependencies: 190
-- Data for Name: reservas_bookingtype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_bookingtype (id, name, description, is_removed, create_date, update_date) FROM stdin;
3	Evento	Reserva en evento	f	2019-09-07 19:18:12.756119-05	2019-09-07 19:18:12.756119-05
4	Normal	Reserva en normal	f	2019-09-07 19:18:12.756119-05	2019-09-07 19:18:12.756119-05
\.


--
-- TOC entry 2221 (class 0 OID 0)
-- Dependencies: 189
-- Name: reservas_bookingtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_bookingtype_id_seq', 4, true);


--
-- TOC entry 2196 (class 0 OID 50433)
-- Dependencies: 194
-- Data for Name: reservas_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_room (id, descripcion, path_image, calificacion, num_camas, num_adultos, num_ninos, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, id_roomtype_id) FROM stdin;
12	Habitación 2	https://images.ctfassets.net/sahy2rpqbnsp/72buNpf6rmGWSMeWokguqM/1f4085ffa6bf582e7c6f9425c1b16cc2/City-2Queen-beds-window-NEW-wide.jpg?w=1920&h=1080&fm=jpg&q=50&fit=fill	0	3	2	1	120	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	2
14	Habitación 4	https://www.camelbackresort.com/upload/photos/lodging_h1_wv_uk_psl6_k---04.10.2018_08.42.17.jpg	0	1	2	0	80	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	3
15	Habitación 5	https://teighmore-assets.s3.amazonaws.com/media/filer_public_thumbnails/filer_public/f8/43/f8437568-8cd3-402f-87cd-27919c2d897f/rooms-and-suites-main-image.jpg__954x493_q85_crop_subsampling-2_upscale.jpg	0	1	1	0	90	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	4
16	Habitación 6	https://www.kalahariresorts.com/media/1838/hut-block.jpg	0	2	1	1	100	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	2
19	Habitación 9	https://cdn.galaxy.tf/unit-media/tc-default/uploads/images/room_photo/001/545/140/queen-vista-sjjxcq9z8qkvrruo8hu-9wu18q0ablzbh-rgb-hd-result-wide.jpg	0	2	2	1	100	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	4
20	Habitación 10	https://amp.businessinsider.com/images/5527f47fdd0895c44f8b459e-750-422.jpg	0	1	2	2	90	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	4
18	Habitación 8	https://secure.cdn1.wdpromedia.com/resize/mwImage/1/560/216/75/dam/wdpro-assets/aulani/room-offers/resort-room/nbr-standard-view-1-16x9.jpg?1540508656347	0	3	2	2	150	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	1
17	Habitación 7	https://theimperialindia.com/wp-content/uploads/2018/03/Deco-Room_compressed77-1.jpg	0	2	2	2	100	t	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	1
13	Habitación 3	https://www.opalsands.com/getmedia/8766c2d7-9e28-4a37-824e-da6a8101f915/Deluxe_King_Guest_Room_575035_high.jpg?width=3000&height=2000&ext=.jpg&maxsidesize=800	0	1	2	2	80	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	1
11	Habitación 1	http://www.chelseatoronto.com/en/uploads/images/2015/06/club-room.jpg	0	2	2	2	100	f	f	2019-09-07 14:21:18.292348-05	2019-09-07 14:21:18.292348-05	1
\.


--
-- TOC entry 2222 (class 0 OID 0)
-- Dependencies: 193
-- Name: reservas_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_room_id_seq', 20, true);


--
-- TOC entry 2194 (class 0 OID 50425)
-- Dependencies: 192
-- Data for Name: reservas_roomtype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_roomtype (id, nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) FROM stdin;
1	Suite	Habitación de tipo suite	f	2019-09-07 14:19:40.210659-05	2019-09-07 14:19:40.210659-05
2	Familiar	Habitación de tipo familiar	f	2019-09-07 14:19:40.210659-05	2019-09-07 14:19:40.210659-05
3	Deluxe	Habitación de tipo deluxe	f	2019-09-07 14:19:40.210659-05	2019-09-07 14:19:40.210659-05
4	Clásico	Habitación de tipo clásico	f	2019-09-07 14:19:40.210659-05	2019-09-07 14:19:40.210659-05
\.


--
-- TOC entry 2223 (class 0 OID 0)
-- Dependencies: 191
-- Name: reservas_roomtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_roomtype_id_seq', 4, true);


--
-- TOC entry 2038 (class 2606 OID 50389)
-- Name: accesos_cliente_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_cliente
    ADD CONSTRAINT accesos_cliente_email_key UNIQUE (email);


--
-- TOC entry 2040 (class 2606 OID 50385)
-- Name: accesos_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_cliente
    ADD CONSTRAINT accesos_cliente_pkey PRIMARY KEY (id);


--
-- TOC entry 2043 (class 2606 OID 50387)
-- Name: accesos_cliente_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_cliente
    ADD CONSTRAINT accesos_cliente_username_key UNIQUE (username);


--
-- TOC entry 2045 (class 2606 OID 50397)
-- Name: accesos_perfil_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_perfil
    ADD CONSTRAINT accesos_perfil_pkey PRIMARY KEY (id);


--
-- TOC entry 2047 (class 2606 OID 50399)
-- Name: accesos_perfil_usuario_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_perfil
    ADD CONSTRAINT accesos_perfil_usuario_id_key UNIQUE (usuario_id);


--
-- TOC entry 2035 (class 2606 OID 50374)
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 2060 (class 2606 OID 50449)
-- Name: reservas_booking_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking
    ADD CONSTRAINT reservas_booking_pkey PRIMARY KEY (id);


--
-- TOC entry 2049 (class 2606 OID 50414)
-- Name: reservas_bookingstate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_bookingstate
    ADD CONSTRAINT reservas_bookingstate_pkey PRIMARY KEY (id);


--
-- TOC entry 2051 (class 2606 OID 50422)
-- Name: reservas_bookingtype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_bookingtype
    ADD CONSTRAINT reservas_bookingtype_pkey PRIMARY KEY (id);


--
-- TOC entry 2056 (class 2606 OID 50441)
-- Name: reservas_room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_room
    ADD CONSTRAINT reservas_room_pkey PRIMARY KEY (id);


--
-- TOC entry 2053 (class 2606 OID 50430)
-- Name: reservas_roomtype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_roomtype
    ADD CONSTRAINT reservas_roomtype_pkey PRIMARY KEY (id);


--
-- TOC entry 2036 (class 1259 OID 50401)
-- Name: accesos_cliente_email_210a8f5e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX accesos_cliente_email_210a8f5e_like ON public.accesos_cliente USING btree (email varchar_pattern_ops);


--
-- TOC entry 2041 (class 1259 OID 50400)
-- Name: accesos_cliente_username_12510d69_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX accesos_cliente_username_12510d69_like ON public.accesos_cliente USING btree (username varchar_pattern_ops);


--
-- TOC entry 2057 (class 1259 OID 50484)
-- Name: reservas_booking_bookingtype_id_id_c544d4f4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX reservas_booking_bookingtype_id_id_c544d4f4 ON public.reservas_booking USING btree (bookingtype_id_id);


--
-- TOC entry 2058 (class 1259 OID 50490)
-- Name: reservas_booking_customer_id_id_5c82b92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX reservas_booking_customer_id_id_5c82b92e ON public.reservas_booking USING btree (customer_id_id);


--
-- TOC entry 2061 (class 1259 OID 50496)
-- Name: reservas_booking_room_id_id_eee9e00c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX reservas_booking_room_id_id_eee9e00c ON public.reservas_booking USING btree (room_id_id);


--
-- TOC entry 2062 (class 1259 OID 50482)
-- Name: reservas_booking_state_id_id_e0c51742; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX reservas_booking_state_id_id_e0c51742 ON public.reservas_booking USING btree (state_id_id);


--
-- TOC entry 2054 (class 1259 OID 50461)
-- Name: reservas_room_id_roomtype_id_5fb6ac48; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX reservas_room_id_roomtype_id_5fb6ac48 ON public.reservas_room USING btree (id_roomtype_id);


--
-- TOC entry 2063 (class 2606 OID 50402)
-- Name: accesos_perfil_usuario_id_9bf61438_fk_accesos_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesos_perfil
    ADD CONSTRAINT accesos_perfil_usuario_id_9bf61438_fk_accesos_cliente_id FOREIGN KEY (usuario_id) REFERENCES public.accesos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2067 (class 2606 OID 50485)
-- Name: reservas_booking_bookingtype_id_id_c544d4f4_fk_reservas_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking
    ADD CONSTRAINT reservas_booking_bookingtype_id_id_c544d4f4_fk_reservas_ FOREIGN KEY (bookingtype_id_id) REFERENCES public.reservas_bookingtype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2068 (class 2606 OID 50491)
-- Name: reservas_booking_customer_id_id_5c82b92e_fk_accesos_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking
    ADD CONSTRAINT reservas_booking_customer_id_id_5c82b92e_fk_accesos_cliente_id FOREIGN KEY (customer_id_id) REFERENCES public.accesos_cliente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2065 (class 2606 OID 50497)
-- Name: reservas_booking_room_id_id_eee9e00c_fk_reservas_room_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking
    ADD CONSTRAINT reservas_booking_room_id_id_eee9e00c_fk_reservas_room_id FOREIGN KEY (room_id_id) REFERENCES public.reservas_room(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2066 (class 2606 OID 50477)
-- Name: reservas_booking_state_id_id_e0c51742_fk_reservas_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_booking
    ADD CONSTRAINT reservas_booking_state_id_id_e0c51742_fk_reservas_ FOREIGN KEY (state_id_id) REFERENCES public.reservas_bookingstate(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2064 (class 2606 OID 50456)
-- Name: reservas_room_id_roomtype_id_5fb6ac48_fk_reservas_roomtype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservas_room
    ADD CONSTRAINT reservas_room_id_roomtype_id_5fb6ac48_fk_reservas_roomtype_id FOREIGN KEY (id_roomtype_id) REFERENCES public.reservas_roomtype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2019-09-08 09:52:13

--
-- PostgreSQL database dump complete
--

