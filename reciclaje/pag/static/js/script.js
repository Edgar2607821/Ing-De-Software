// Función que se ejecuta cuando se selecciona un dispositivo en el formulario
const filtrarTipos = async (idDispositivo) => {
    try {
        const csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
        const headers = { "X-CSRFToken": csrfTokenValue };
        const response = await axios.post("/filtrar-tipos/", { dispositivo_id: idDispositivo }, { headers });

        const { data, status } = response;
        if (status === 200) {
            let selectTipo = document.querySelector("#Tipos");
            selectTipo.innerHTML = "";

            // Crear opción por defecto
            const defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.text = "Seleccione";
            selectTipo.appendChild(defaultOption);

            // Iterar sobre los datos para agregar tipos al select
            data.data.forEach((item) => {
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.tipo;
                selectTipo.appendChild(option);
            });
        } else {
            console.error("Error al obtener tipos de dispositivo");
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
    }
};

// Función que se ejecuta cuando se selecciona un tipo en el formulario
const filtrarMarcas = async (idTipo) => {
    try {
        const csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
        const headers = { "X-CSRFToken": csrfTokenValue };
        const response = await axios.post("/filtrar-marcas/", { tipo_id: idTipo }, { headers });

        const { data, status } = response;
        if (status === 200) {
            let selectMarca = document.querySelector("#Marcas");
            selectMarca.innerHTML = "";

            // Crear opción por defecto
            const defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.text = "Seleccione";
            selectMarca.appendChild(defaultOption);

            // Iterar sobre los datos para agregar marcas al select
            data.data.forEach((item) => {
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.nombre;
                selectMarca.appendChild(option);
            });
        } else {
            console.error("Error al obtener marcas de dispositivo");
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
    }
};

// Función que se ejecuta cuando se selecciona una marca en el formulario
const filtrarModelos = async (idMarca) => {
    try {
        const csrfTokenValue = document.querySelector("[name=csrfmiddlewaretoken]").value;
        const headers = { "X-CSRFToken": csrfTokenValue };
        const response = await axios.post("/filtrar-modelos/", { marca_id: idMarca }, { headers });

        const { data, status } = response;
        if (status === 200) {
            let selectModelo = document.querySelector("#Modelos");
            selectModelo.innerHTML = "";

            // Crear opción por defecto
            const defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.text = "Seleccione";
            selectModelo.appendChild(defaultOption);

            // Iterar sobre los datos para agregar modelos al select
            data.data.forEach((item) => {
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.nombre;
                selectModelo.appendChild(option);
            });
        } else {
            console.error("Error al obtener modelos de dispositivo");
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
    }
};
