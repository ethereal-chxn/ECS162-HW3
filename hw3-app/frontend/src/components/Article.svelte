<script lang="js">
  import CommentsButton from "./CommentsButton.svelte";
  let { articleInfo, id, clickHandler } = $props();
</script>

<article>
  <!-- Extract article headline from JSON object  -->
  <h2>{articleInfo.headline.main}</h2>
  <!-- Extract article image and alt text from JSON object -->
  <img
    src={articleInfo.multimedia.default.url}
    alt={articleInfo.multimedia.caption}
  />
  <!-- Extract article tagline from JSON object -->
  <p>{articleInfo.abstract}</p>
  <CommentsButton articleId={id} clickHandler={clickHandler}/>
</article>
