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