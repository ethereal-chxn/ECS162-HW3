<script lang="ts">
  import { onMount } from "svelte";
  import Column from "./components/Column.svelte";
  import CommentSection from "./components/CommentSection.svelte";
  import AccountButton from "./components/AccountButton.svelte";

  let apiKey = $state("");
  let url = $state("");
  let articles: any[] = $state([]);
  let currArticleDisplayed = $state(-1)
  let currCommentsDisplayed = $state({});
  let isShowingComments = $state(false);
  let isLoggedIn = $state(false);

  /* Event Listeners */
  // Pressing the comments button on an article
  async function onCommentsButtonPressed(articleId: number) {
    // Open sidebar
    isShowingComments = true;
    currArticleDisplayed = articleId;

    // Display comments for article
    const commentsInArticle = await retrieveCommentsInArticle(articleId);
    currCommentsDisplayed = commentsInArticle;
  }

  // Pressing the X buttton on the comments sidebar closes the sidebar
  function onCloseCommentsPressed() {
    isShowingComments = false;
  }
  
  // Pressing the LOG IN button brings user to dex sign-in
  async function onLoginPressed() {
    window.location.href = "http://localhost:8000/login";
    isLoggedIn = true;
  }

  async function retrieveCommentsInArticle(articleId: number) {
    const commentsInArticle = await fetch(`http://localhost:8000/api/comments/article/${articleId}`);
    console.log(commentsInArticle);
    return commentsInArticle;
  }

  onMount(async () => {
    try {
      const res = await fetch("/api/key");
      const data = await res.json();
      apiKey = data.apiKey;
      url = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q=(Sacramento,Davis)%sort=newest&api-key=${apiKey}`;
    } catch (error) {
      console.error("Failed to fetch API key:", error);
    }

    await fetch(url)
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        console.log(data.response.docs);
        articles = data.response.docs;
      })
      .catch((error) => {
        console.error("Error fetching data >~<: ", error);
      });
  });

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  const currDate = new Date();
  // getMonth() returns an integer 0-11.
  // Using the output of getMonth() to index
  // an array of month names allows us to get
  // corresponding month name.
  let currMonth = months[currDate.getMonth()];
  // Same logic described above applies here.
  let currDay = days[currDate.getDay()];
</script>


{#if isShowingComments}
<div class="sidebar" style="width:25%;right:0">
  <CommentSection 
    articleId={currArticleDisplayed} 
    onClickHandler={onCloseCommentsPressed} 
    comments={currCommentsDisplayed}
  />
</div>
{/if}

<header>
  <section class="header-section">
    <!--
    Webpage Title
    -->
    <h1>The New York Times</h1>
    <!--
    Dynamic Current Date Display
    -->
    <div id="date-and-account">
      <p id="curr-date">
        {currDay +
          ", " +
          currMonth +
          " " +
          currDate.getDate() +
          ", " +
          currDate.getFullYear()}
      </p>
      <div id="account">
        {#if isLoggedIn}
          <p>Account</p>
        {:else}
          <AccountButton clickHandler={onLoginPressed}/>
        {/if}
    </div>
  </div>
  </section>
</header>

<main>
  <section class="articles-section">
    <Column articles={articles.slice(0, 2)} idList={[0, 1]} clickHandler={onCommentsButtonPressed}/>
    <Column articles={articles.slice(2, 4)} idList={[2, 3]} clickHandler={onCommentsButtonPressed}/>
    <Column articles={articles.slice(4, 6)} idList={[4, 5]} clickHandler={onCommentsButtonPressed}/>
  </section>
</main>
