<script>
    import DeleteButton from "./DeleteButton.svelte";
    let { commentId, author, commentBody, isModerator } = $props()
</script>

<div class="comment">
    <h2>{author}</h2>
    <p>{commentBody}</p>
    {#if isModerator}
        <DeleteButton commentId={commentId}/>
    {/if}
</div>
