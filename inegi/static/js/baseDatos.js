var db;
		$(document).ready( function(){

					 db = openDatabase("Inegi", "1.0", "Base de datos para el manejo de parches en la plataforma windows", "200000");

					//alert("La base de datos ha sido creada");

					crearTabla(); 
				
		});

		function crearTabla(){


			db.transaction( function(t){

				t.executeSql('CREATE TABLE IF NOT EXISTS EQUIPOS(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, EQUIPO TEXT)',[],showRecords, handleError);

			});
		function showRecords(){


			//Hacer algo
		}


		function handleError(e){
			alert('Error while table' + e);
		}


		}
