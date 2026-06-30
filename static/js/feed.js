function showToast(message) {
        const toast = document.getElementById("toast");
        if (!toast) return;
        toast.textContent = message;
        toast.classList.remove("opacity-0");
        toast.classList.add("opacity-100");
        setTimeout(() => {
            toast.classList.remove("opacity-100");
            toast.classList.add("opacity-0");
        }, 2500);
    }

    function sharePost(button) {
        const url = button.dataset.postUrl;
        const author = button.dataset.postAuthor || "a friend";
        const shareData = { title: "Post by " + author, text: "Check out this post on Facebook Clone", url: url };

        if (navigator.share) {
            navigator.share(shareData).catch(() => {});
        } else if (navigator.clipboard) {
            navigator.clipboard.writeText(url).then(() => {
                showToast("Post link copied to clipboard!");
            }).catch(() => {
                showToast("Could not copy link.");
            });
        } else {
            showToast(url);
        }
    }
    
    document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("post-picture-input");
    const fileName = document.getElementById("selected-file-name");

    if (!fileInput || !fileName) return;

    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
            fileName.textContent = fileInput.files[0].name;
        } else {
            fileName.textContent = "No file selected";
        }
    });
});
