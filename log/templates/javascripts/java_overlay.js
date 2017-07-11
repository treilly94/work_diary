document.getElementById("createblog_button").onclick = function () {
        location.href = "{% url 'createblog' %}";
    };
}