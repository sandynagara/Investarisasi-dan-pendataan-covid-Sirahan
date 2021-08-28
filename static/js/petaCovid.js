function kuisioner(object) {
    var div = document.createElement("div");
    div.classList.add("kuisioner");

    var label = document.createElement("label");
    label.classList.add("form-check-label");

    var teks = document.createTextNode(object.pertanyaan);
    label.classList.add("tanya");
    label.appendChild(teks);

    var divPilihan = document.createElement("div");
    divPilihan.classList.add("pilihan");
    divPilihan.appendChild(check(object.name, true, "Ya"));
    divPilihan.appendChild(check(object.name, false, "Tidak"));

    div.appendChild(label);
    div.appendChild(divPilihan);
    var query = document.body.querySelector("div#tes");
    query.appendChild(div);
}

function check(name, kondisi, teks) {
    var div = document.createElement("div");
    div.classList.add("form-check");
    div.appendChild(radio(name, kondisi));
    div.appendChild(label(teks));
    return div;
}

function label(isiTeks) {
    var label = document.createElement("label");
    label.classList.add("form-check-label");

    var teks = document.createTextNode(isiTeks);
    label.appendChild(teks);
    return label;
}

function radio(name, kondisi) {
    var input = document.createElement("input");
    input.classList.add("form-check-inputZ");
    input.setAttribute("type", "radio");
    input.setAttribute("name", name);
    input.setAttribute("value", kondisi);
    if (kondisi == true) {
        input.setAttribute("checked", kondisi);
    }
    return input;
}

var daftar = [{
        pertanyaan: "Demam",
        name: "Demam",
    },
    {
        pertanyaan: "Batuk / Pilek",
        name: "Pilek",
    },
    {
        pertanyaan: "Sesak nafas",
        name: "bernafas",
    },
    {
        pertanyaan: "Nyeri tenggorokan",
        name: "tenggorokan",
    },
    {
        pertanyaan: "Lama penyakit kurang dari 14 hari",
        name: "Lama",
    },
    {
        pertanyaan: "Kontak erat dengan penderita COVID-19",
        name: "kontak",
    },
    {
        pertanyaan: "Riwayat ke area penularan lokal",
        name: "tinggal",
    },
];

window.onload = function () {
    
     $("#exampleModalCenter").modal("show");
    
    for (var index = 0; index < daftar.length; index++) {
        kuisioner(daftar[index]);
    }

    var map = L.map("map", {
        center: [-7.618663, 110.268112],
        zoom: 22,
    });

    var map2 = L.map("map2", {
        center: [-7.618663, 110.268112],
        zoom: 22,
    });

    var esri = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
            attribution: "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
            maxNativeZoom:15,
            maxZoom:25
        }
    );

    var esri2 = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", {
            attribution: "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
            maxNativeZoom:17,
            maxZoom:25
        }
    );

    var posisi = L.marker([-7.618663, 110.268112], {
        draggable: true,
    }).addTo(map2);

    var lintang, bujur;

    var gambar = document.getElementById("pic-src");

    var LeafIcon = L.Icon.extend({
        options: {
            iconSize: [48, 50],
            iconAnchor: [12, 41],
            shadowAnchor: [4, 62],
            popupAnchor: [-3, -76],
        },
    });

    var iconMarker = new LeafIcon({
        iconUrl: gambar.value
    });

    console.log(iconMarker, "tes");

    posisi.on("dragend", function (e) {
        lintang = document.getElementById("Lintang").value = posisi.getLatLng().lat;
        bujur = document.getElementById("Bujur").value = posisi.getLatLng().lng;
    });

    $("#tambah").on("shown.bs.modal", function () {
        map2.invalidateSize();
    });

    esri.addTo(map);
    esri2.addTo(map2);

    map.on("map:loadfield", function (e) {
        // Customize map for field
        console.log(e.field, e.fieldid);
    });

    console.log(daftarCovid);

    var info = document.getElementsByClassName("isi");

    var layerGroup = L.layerGroup().addTo(map);
    for (var i = 0; i < daftarCovid.length; i++) {
        marker = new L.marker([
            daftarCovid[i].fields.latitude,
            daftarCovid[i].fields.longitude,
        ],{icon : iconMarker});

        marker.feature = {
            type: "Point",
            properties: {
                nama: daftarCovid[i].fields.nama,
                usia: daftarCovid[i].fields.usia,
                nomorHP: daftarCovid[i].fields.nomorHp,
                tesCovid: daftarCovid[i].fields.tesCovid,
                demam: daftarCovid[i].fields.demam,
                pilek: daftarCovid[i].fields.pilek,
                bernafas: daftarCovid[i].fields.bernafas,
                tenggorokan: daftarCovid[i].fields.tenggorokan,
                lamaPenyakit: daftarCovid[i].fields.lamaPenyakit,
                kontak: daftarCovid[i].fields.kontak,
                tinggal: daftarCovid[i].fields.tinggal,
            },
        };

        marker.on("click", function (e) {
            var nama = e.target.feature.properties.nama,
                usia = e.target.feature.properties.usia,
                nomorHP = e.target.feature.properties.nomorHP,
                tesCovid = e.target.feature.properties.tesCovid,
                demam = e.target.feature.properties.demam,
                pilek = e.target.feature.properties.pilek,
                bernafas = e.target.feature.properties.bernafas,
                tenggorokan = e.target.feature.properties.tenggorokan,
                lamaPenyakit = e.target.feature.properties.lamaPenyakit,
                kontak = e.target.feature.properties.kontak,
                tinggal = e.target.feature.properties.tinggal;

            console.log(e.latlng);
            console.log(e);

            info[0].innerHTML = "<p>" + nama + "</p>";
            info[1].innerHTML = "<p>" + usia + "</p>";
            info[2].innerHTML = "<p>" + nomorHP + "</p>";
            info[3].innerHTML =
                "<p>" + check2(tesCovid) + "</p>";
            info[4].innerHTML =
                "<p>" + check2(demam) + "</p>";
            info[5].innerHTML =
                "<p>" + check2(pilek) + "</p>";
            info[6].innerHTML =
                "<p>" + check2(bernafas) + "</p>";
            info[7].innerHTML =
                "<p>" + check2(tenggorokan) + "</p>";
            info[8].innerHTML =
                "<p>" + check2(lamaPenyakit) + "</p>";
            info[9].innerHTML =
                "<p>" + check2(kontak) + "</p>";
            info[10].innerHTML =
                "<p>" + check2(tinggal) + "</p>";

            var label = document.getElementById("vonis");
            var b = document.createElement("b");
            var query = document.querySelector("b#vonis")
            console.log(query)
            var vonisData = document.createTextNode(vonis(tesCovid,demam,pilek,bernafas,tenggorokan,lamaPenyakit,kontak,tinggal)) 
            b.appendChild(vonisData)
            query.innerHTML = vonis(tesCovid,demam,pilek,bernafas,tenggorokan,lamaPenyakit,kontak,tinggal)
       

            $("#info").modal("show");
        });


        layerGroup.addLayer(marker);
    }

    function check2(kondisi) {
        if (kondisi == true) {
            return "Ya";
        } else {
            return "Tidak";
        }
    }

    function vonis(tesCovid,demam,pilek,bernafas,tenggorokan,lamaPenyakit,kontak,tinggal) {
        if(tesCovid){
           if(demam == true || pilek == true || bernafas == true ){
               return "Konfirmasi dengan gejala"
           }else{
                return "Konfirmasi tanpa gejala"
           }
        }else{
            if(kontak == true || tinggal == true){
                if(demam == true || pilek == true || bernafas == true ){
                    return "Suspek / Pelaku Perjalanan dengan gejala"
                }else{
                    return "Suspek / Pelaku Perjalanan tanpa gejala"
                }
            }else {
                return "Sehat"
            }
        }
        return "Berdasarkan hasil kuisioner maka pasien kemungkinan termasuk kategori ";
    }
};