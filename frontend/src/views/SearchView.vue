<template>
  <!-- <progress
    class="progress progress-primary w-full px-10 mt-10"
    value="50"
    max="100"
  ></progress>

 <form>
    <section>
      <h3>Step 1</h3>
    </section>

    <section>
      <h3>Step 2</h3>
    </section>

    <section>
      <h3>Step 3</h3>
    </section>
  </form> -->

  <SearchForm />
</template>

<script>
import SearchForm from "../components/SearchForm.vue";
export default {
  components: { SearchForm },
  setup() {
    let questions = [
      "The smartphone you are looking for is it for you or for someone else?",
      "How much time per day do you spend on your smartphone?",
      "Usually, you use your smartphone for:",
    ];

    let answers = [
      [
        "For me",
        "For someone else",
        "For me and for someone else",
        "I don't know",
      ],
      ["Less than 1 hour", "1-2 hours", "2-3 hours", "More than 3 hours"],
      [
        "Social media",
        "Gaming",
        "Watching videos",
        "Taking photos",
        "Listening to music",
        "Reading",
        "Other",
      ],
    ];

    return {
      questions,
      answers,
    };
  },
};
</script>
