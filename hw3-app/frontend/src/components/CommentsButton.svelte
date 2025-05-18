<script>
    let articleId = $props();

    async function fetchCommentsInArticle(articleId) {

    }
</script>

<button id="comment-button">
    <div id="comment-button-content">
        <img 
            id="comment-icon" 
            src="/src/assets/comment-icon.png" 
            alt="comment icon" 
            on:click={fetchCommentsInArticle, articleId}
        >
    </div>
</button>