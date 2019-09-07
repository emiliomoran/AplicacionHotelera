/*RoomType */
select * from reservas_roomtype;
delete from reservas_roomtype;

insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Suite','Habitación de tipo suite', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Familiar','Habitación de tipo familiar', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Deluxe','Habitación de tipo deluxe', false, now(), now());
insert into reservas_roomtype(nombre, descripcion, eliminado, fecha_creacion, fecha_modificacion) values('Clásico','Habitación de tipo clásico', false, now(), now());
/* */

/*Room */
select * from reservas_room;
delete from reservas_room;

insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(16, 'Habitación 1', 2, 100, true, false, now(), now(), 2, 2, 0, 'http://www.chelseatoronto.com/en/uploads/images/2015/06/club-room.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(17, 'Habitación 2', 3, 120, true, false, now(), now(), 2, 1, 0, 'https://images.ctfassets.net/sahy2rpqbnsp/72buNpf6rmGWSMeWokguqM/1f4085ffa6bf582e7c6f9425c1b16cc2/City-2Queen-beds-window-NEW-wide.jpg?w=1920&h=1080&fm=jpg&q=50&fit=fill');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(16, 'Habitación 3', 1, 80, true, false, now(), now(), 2, 3, 0, 'https://www.opalsands.com/getmedia/8766c2d7-9e28-4a37-824e-da6a8101f915/Deluxe_King_Guest_Room_575035_high.jpg?width=3000&height=2000&ext=.jpg&maxsidesize=800');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(18, 'Habitación 4', 1, 80, true, false, now(), now(), 2, 0, 0, 'https://www.camelbackresort.com/upload/photos/lodging_h1_wv_uk_psl6_k---04.10.2018_08.42.17.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(19, 'Habitación 5', 1, 90, true, false, now(), now(), 1, 0, 0, 'https://teighmore-assets.s3.amazonaws.com/media/filer_public_thumbnails/filer_public/f8/43/f8437568-8cd3-402f-87cd-27919c2d897f/rooms-and-suites-main-image.jpg__954x493_q85_crop_subsampling-2_upscale.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(17, 'Habitación 6', 2, 100, true, false, now(), now(), 1, 1, 0, 'https://www.kalahariresorts.com/media/1838/hut-block.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(16, 'Habitación 7', 2, 100, true, false, now(), now(), 2, 1, 0, 'https://theimperialindia.com/wp-content/uploads/2018/03/Deco-Room_compressed77-1.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(16, 'Habitación 8', 3, 150, true, false, now(), now(), 2, 2, 0, 'https://secure.cdn1.wdpromedia.com/resize/mwImage/1/560/216/75/dam/wdpro-assets/aulani/room-offers/resort-room/nbr-standard-view-1-16x9.jpg?1540508656347');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(19, 'Habitación 9', 2, 100, true, false, now(), now(), 2, 1, 0, 'https://cdn.galaxy.tf/unit-media/tc-default/uploads/images/room_photo/001/545/140/queen-vista-sjjxcq9z8qkvrruo8hu-9wu18q0ablzbh-rgb-hd-result-wide.jpg');
insert into reservas_room(id_roomtype_id, descripcion, num_camas, precio, disponible, eliminado, fecha_creacion, fecha_modificacion, num_adultos, num_ninos, calificacion, path_image) values(19, 'Habitación 10', 1, 90, true, false, now(), now(), 2, 2, 0, 'https://amp.businessinsider.com/images/5527f47fdd0895c44f8b459e-750-422.jpg');
/* */


