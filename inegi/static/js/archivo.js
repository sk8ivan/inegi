function inicio(){

	alert("Funcionando");
}

function soporteFile(){

	if (typeof window.FileReader!=="undefined")
	{
	// Soportado el File API
	alert("El navegadro soporta la API de archivos")
	}
	else
	{
	// No es soportado el File API
		alert("El navegador no soporta la API de archivos :C")
	}
}

function processFiles(files) {
	var file = files[0];

	var reader = new FileReader();

		reader.onload = function (e) {
			// Cuando éste evento se dispara, los datos están ya disponibles.
			// Se trata de copiarlos a una área <div> en la página.
			var output = document.getElementById("celda");
			var nombre = file.name;
			var separacion =nombre.split('.');

			output.textContent = separacion[0] + " 05/01/2015";
			//e.target.result;
			//return file.name.split(".");

			 
		};
	
	reader.readAsText(file);
}

function imprimir(separacion){

	var parche = document.getElementById("1");
	console.log(parche.textContent);
	if (parche.textContent == "KB2761451")
	{
		//document.write("Equipo de ivan");
		//creando nueva tabla
		var celda = document.createElement("td");
		celda.textContent = "Equipo de Iván";
		//var tabla = Element.getElementsByTagName("tr");
		//parche.appendChild(separacion[0]);

	}else
	{

		document.write("No se encontro nada :C")
	};


}
//tutorail api file http://robertnyman.com/2010/12/16/utilizing-the-html5-file-api-to-choose-upload-preview-and-see-progress-for-multiple-files/
