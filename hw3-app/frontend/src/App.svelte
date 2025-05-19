<script lang="ts">
  import { onMount, setContext } from "svelte";
  import Column from "./components/Column.svelte";
  import CommentSection from "./components/CommentSection.svelte";
  import AccountButton from "./components/AccountButton.svelte";
  import AccountTab from "./components/AccountTab.svelte";

  let apiKey = $state("");
  let url = $state("");
  let articles: any[] = $state([]);
  let currArticleDisplayed = $state(-1)
  let currCommentsDisplayed = $state({});
  let isShowingComments = $state(false);
  let isShowingAccountTab = $state(false);
  let isLoggedIn = $state(false);
  let isModerator = $state(false);
  let userEmail = $state("");


  /* Event Listeners */

  
  // Pressing the comments button on an article
  async function retrieveCommentsInArticle(articleId: number) {
    const commentsInArticle = await fetch(`http://localhost:8000/api/comments/article/${articleId}`);
    return commentsInArticle.json();
  }

  async function onCommentsButtonPressed(articleId: number) {
    if (!isShowingComments && isLoggedIn) {
      // Open sidebar if not already
      isShowingComments = true;
      currArticleDisplayed = articleId;
    } else {
      isShowingComments = false;
    }

    //Display comments for article
    const commentsInArticle = await retrieveCommentsInArticle(articleId);
    currCommentsDisplayed = commentsInArticle;
  }

  // Pressing the X buttton on the comments sidebar closes the sidebar
  function onCloseCommentsPressed() {
    isShowingComments = false;
  }

  function onAccountTabPressed() {
    isShowingAccountTab = true;
  }

  function onCloseAccountTabPressed() {
    isShowingAccountTab = false;
  }
  
  // Pressing the LOG IN button brings user to dex sign-in
  async function onLoginPressed() {
    window.location.href = "http://localhost:8000/login";
  }

  async function onLogoutPressed() {
    window.location.href = "http://localhost:8000/logout"
  }

  onMount(async () => {
    const newUrl = new URL(window.location.href);
    userEmail = newUrl.searchParams.get('user');
    console.log('Logged in user:', userEmail);

    if (userEmail) {
      isLoggedIn = true;
      setContext("userEmail", userEmail);
      if (userEmail == "moderator@hw3.com") {
        isModerator = true;
      }
    }

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
<div class="sidebar" style="width:35%;right:0">
  <CommentSection 
    articleId={currArticleDisplayed}
    comments={currCommentsDisplayed}
    onClickHandler={onCloseCommentsPressed} 
    isModerator={isModerator}
  />
</div>
{/if}

{#if isShowingAccountTab}
<div class="sidebar" style="width:35%;right:0">
    <AccountTab onExitClick={onCloseAccountTabPressed} onLogoutClick={onLogoutPressed}/>
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
          <button onclick={onAccountTabPressed}>Account</button>
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
