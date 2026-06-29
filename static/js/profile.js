function openImage(src) {
    const modal = document.getElementById("imageModal");
    const image = document.getElementById("modalImage");

    image.src = src;
    modal.style.display = "flex";

    document.body.style.overflow = "hidden";
}

function closeImage() {
    const modal = document.getElementById("imageModal");

    modal.style.display = "none";

    document.body.style.overflow = "";
}

function toggleReply(commentId) {
    const form = document.getElementById("reply-form-" + commentId);
    if (!form) return;

    form.classList.toggle("hidden");

    if (!form.classList.contains("hidden")) {
        const input = form.querySelector("input[name='content']");
        if (input) input.focus();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("imageModal");
    const image = document.getElementById("modalImage");

    if (!modal || !image) return;

    modal.style.display = "none";

    modal.addEventListener("click", closeImage);

    image.addEventListener("click", (e) => {
        e.stopPropagation();
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            closeImage();
        }
    });
});