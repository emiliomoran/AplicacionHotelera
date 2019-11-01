/*Usr */
insert into accesos_usr(last_login, username, email, password, is_admin, is_staff, is_superuser, is_removed, create_date, update_date)
values(now(), 'admin', 'admin@example.com', 'pbkdf2_sha256$150000$A1NCffAdapJu$6WOJc4OM4nb48ctxktlqfsF7olj/j4PlsEYSR4PSJ2o=', false, false, false, false, now(), now());
/* */

/*Perfil */
insert into accesos_perfil(name,cedula, last_name, phone, date_birth, is_removed, create_date, update_date, usr_id_id)
values('admin','0912345678', 'admin', null, now(), false, now(), now(), 1);
/* */

/*RoomType */
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Suite','Habitación de tipo suite', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Familiar','Habitación de tipo familiar', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Deluxe','Habitación de tipo deluxe', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Clásico','Habitación de tipo clásico', false, now(), now());
/* */

/*Room */
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(1, 'Habitación 1', 2, 100, true, false, now(), now(), 2, 2, 0, 'http://www.chelseatoronto.com/en/uploads/images/2015/06/club-room.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(2, 'Habitación 2', 3, 120, true, false, now(), now(), 2, 1, 0, 'https://images.ctfassets.net/sahy2rpqbnsp/72buNpf6rmGWSMeWokguqM/1f4085ffa6bf582e7c6f9425c1b16cc2/City-2Queen-beds-window-NEW-wide.jpg?w=1920&h=1080&fm=jpg&q=50&fit=fill');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(1, 'Habitación 3', 1, 80, true, false, now(), now(), 2, 3, 0, 'https://www.opalsands.com/getmedia/8766c2d7-9e28-4a37-824e-da6a8101f915/Deluxe_King_Guest_Room_575035_high.jpg?width=3000&height=2000&ext=.jpg&maxsidesize=800');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(3, 'Habitación 4', 1, 80, true, false, now(), now(), 2, 0, 0, 'https://www.camelbackresort.com/upload/photos/lodging_h1_wv_uk_psl6_k---04.10.2018_08.42.17.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(4, 'Habitación 5', 1, 90, true, false, now(), now(), 1, 0, 0, 'https://teighmore-assets.s3.amazonaws.com/media/filer_public_thumbnails/filer_public/f8/43/f8437568-8cd3-402f-87cd-27919c2d897f/rooms-and-suites-main-image.jpg__954x493_q85_crop_subsampling-2_upscale.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(2, 'Habitación 6', 2, 100, true, false, now(), now(), 1, 1, 0, 'https://www.kalahariresorts.com/media/1838/hut-block.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(1, 'Habitación 7', 2, 100, true, false, now(), now(), 2, 1, 0, 'https://theimperialindia.com/wp-content/uploads/2018/03/Deco-Room_compressed77-1.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(1, 'Habitación 8', 3, 150, true, false, now(), now(), 2, 2, 0, 'https://secure.cdn1.wdpromedia.com/resize/mwImage/1/560/216/75/dam/wdpro-assets/aulani/room-offers/resort-room/nbr-standard-view-1-16x9.jpg?1540508656347');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(4, 'Habitación 9', 2, 100, true, false, now(), now(), 2, 1, 0, 'https://cdn.galaxy.tf/unit-media/tc-default/uploads/images/room_photo/001/545/140/queen-vista-sjjxcq9z8qkvrruo8hu-9wu18q0ablzbh-rgb-hd-result-wide.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(4, 'Habitación 10', 1, 90, true, false, now(), now(), 2, 2, 0, 'https://amp.businessinsider.com/images/5527f47fdd0895c44f8b459e-750-422.jpg');
/* */

/*Booking type*/
insert into reservas_bookingtype(name, description, is_removed, create_date, update_date) values('Normal', 'Reserva normal', false, now(), now());
insert into reservas_bookingtype(name, description, is_removed, create_date, update_date) values('Evento', 'Reserva evento', false, now(), now());
/* */

/*Booking state*/
insert into public.reservas_bookingstate(name, description, is_removed, create_date, update_date) values('Pasada', 'Reserva pasada', false, now(), now());
insert into public.reservas_bookingstate(name, description, is_removed, create_date, update_date) values('Actual', 'Reserva actual', false, now(), now());
insert into public.reservas_bookingstate(name, description, is_removed, create_date, update_date) values('Futura', 'Reserva futura', false, now(), now());
/* */

/* Booking */
insert into reservas_booking(booking_date, check_in_date, check_out_date, no_nights, is_removed, create_date, update_date, bookingtype_id_id, customer_id_id, room_id_id, state_id_id)
values(now(), '2019-09-05 23:34:39.554642-05', '2019-09-07 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 1, 1),
(now(), '2019-09-01 21:34:39.554642-05', '2019-09-03 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 2, 1),
(now(), '2019-09-05 23:34:39.554642-05', '2019-09-07 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 9, 1),
(now(), '2019-09-07 21:34:39.554642-05', '2019-09-07 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 8, 1),
(now(), '2019-09-07 21:34:39.554642-05', '2019-09-07 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 6, 1),
(now(), '2019-09-08 21:34:39.554642-05', '2019-09-10 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 2, 2),
(now(), '2019-09-08 21:34:39.554642-05', '2019-09-10 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 3, 2),
(now(), '2019-09-09 21:34:39.554642-05', '2019-09-10 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 4, 3),
(now(), '2019-09-08 21:34:39.554642-05', '2019-09-10 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 1, 2),
(now(), '2019-09-10 21:34:39.554642-05', '2019-09-14 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 5, 3),
(now(), '2019-09-15 21:34:39.554642-05', '2019-09-07 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 10, 3),
(now(), '2019-09-08 21:34:39.554642-05', '2019-09-11 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 9, 2),
(now(), '2019-09-12 21:34:39.554642-05', '2019-09-14 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 1, 3),
(now(), '2019-09-20 21:34:39.554642-05', '2019-09-21 21:34:39.554642-05', 2, false, now(), now(), 1, 1, 3, 3);
/* */

/* Tour_Package */
INSERT INTO public.tour_package_tour_package(
	id, titulo, descripcion, precio)
	VALUES (1,'Paquete 1','Nadar con tortugas',100),
	(2, 'Paquete 2', 'Tour a las Islas', 300);