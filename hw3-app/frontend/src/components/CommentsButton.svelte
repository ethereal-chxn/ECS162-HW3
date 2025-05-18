<script>
    let {articleId, clickHandler} = $props();
</script>

<button id="comment-button" onclick={() => {clickHandler(articleId)}}>
    <div id="comment-button-content">
        <img 
            id="comment-icon" 
            src="/src/assets/comment-icon.png" 
            alt="comment icon" 
        >
    </div>
</button>