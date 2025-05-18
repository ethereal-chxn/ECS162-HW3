<script lang="js">
  let { articleInfo } = $props();
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
  <!-- <button></button> -->
</article>
