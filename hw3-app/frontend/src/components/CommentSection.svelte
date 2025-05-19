<script lang="js">
  import { onMount } from "svelte";
  import CommentBox from "./CommentBox.svelte";
  import Comment from "./Comment.svelte";

  let {articleId, onClickHandler, comments, isModerator} = $props();
</script>

<section class="comment-section">
  <div class="comment-section-header">
    <button class="exit-button" onclick={onClickHandler}>×</button>
  </div>

  <h2>Comments</h2>

  <CommentBox articleId={articleId}/>

  {#each comments["comments"] as comment}
    <Comment
      commentId={comment["_id"]} 
      author={comment["author"]} 
      commentBody={comment["commentBody"]}
      isModerator={isModerator}
    /> 
  {/each}
</section>
