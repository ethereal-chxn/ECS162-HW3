<script>
    let {commentId} = $props();

    async function deleteComment(id) {
        const res = await fetch(`http://localhost:8000/api/comments/${id}`, {method: "DELETE", mode: "cors"});
        console.log(await res.json());
        window.location.reload();
    }

</script>

<button id="delete-button" onclick={() => {deleteComment(commentId)}}>
    Delete
</button>

