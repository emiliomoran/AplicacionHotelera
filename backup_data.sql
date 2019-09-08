--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

-- Started on 2019-09-08 09:53:53

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2186 (class 0 OID 50377)
-- Dependencies: 184
-- Data for Name: accesos_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accesos_cliente (id, last_login, nombres, apellidos, fecha_nacimiento, username, email, password, estado, fecha_creacion, fecha_modificacion, is_staff, is_superuser) FROM stdin;
1	\N	emilio	morán pilligua	2019-09-06	\N	emiliojmp9@gmail.com	pbkdf2_sha256$150000$BEdO3YK8SQCn$Ph3RXbimSg2Vpcc2ZafNKAbESahtZK7tKuRuZ76PqFo=	t	2019-09-07 19:51:22.586014-05	2019-09-07 19:51:22.586014-05	f	f
\.


--
-- TOC entry 2204 (class 0 OID 0)
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
-- TOC entry 2205 (class 0 OID 0)
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
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 5, true);


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
-- TOC entry 2192 (class 0 OID 50417)
-- Dependencies: 190
-- Data for Name: reservas_bookingtype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas_bookingtype (id, name, description, is_removed, create_date, update_date) FROM stdin;
3	Evento	Reserva en evento	f	2019-09-07 19:18:12.756119-05	2019-09-07 19:18:12.756119-05
4	Normal	Reserva en normal	f	2019-09-07 19:18:12.756119-05	2019-09-07 19:18:12.756119-05
\.


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
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 195
-- Name: reservas_booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_booking_id_seq', 45, true);


--
-- TOC entry 2208 (class 0 OID 0)
-- Dependencies: 187
-- Name: reservas_bookingstate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_bookingstate_id_seq', 3, true);


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 189
-- Name: reservas_bookingtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_bookingtype_id_seq', 4, true);


--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 193
-- Name: reservas_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_room_id_seq', 20, true);


--
-- TOC entry 2211 (class 0 OID 0)
-- Dependencies: 191
-- Name: reservas_roomtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservas_roomtype_id_seq', 4, true);


-- Completed on 2019-09-08 09:53:53

--
-- PostgreSQL database dump complete
--

