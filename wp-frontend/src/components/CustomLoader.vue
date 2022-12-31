<template>
  <div
    class="fixed top-0 left-0 right-0 bottom-0 w-full h-screen z-50 overflow-hidden bg-gray-900/90 flex flex-col items-center justify-center"
  >
    <div
      class="rounded grid grid-row-3 overflow-hidden bg-white shadow-lg w-2/3 h-2/6"
    >
      <!-- <div class="bg-white"> -->
      <div>
        <h2 class="text-center text-gray-900 pt-10 text-4xl font-semibold my-2">
          <span class="animate-pulse mr-2">Loading</span>
          <span class="blinke-dot mr-2">.</span>
          <span class="blinke-dot mr-2">.</span>
          <span class="blinke-dot mr-2">.</span>
        </h2>
      </div>

      <div class="flex mx-auto pb-3">
        <div
          class="dash first-dash bg-teal-accent-400 rounded-lg shadow-2xl shadow-white mx-5 my-0 h-4 w-9 animate-first-spin duration-200 origin-center origin-right"
        ></div>
        <div
          class="dash second-dash bg-teal-accent-400 rounded-lg shadow-2xl shadow-white mx-5 my-0 h-4 w-9 animate-second-spin duration-300 origin-center origin-right"
        ></div>
        <div
          class="dash third-dash bg-teal-accent-400 rounded-lg shadow-2xl shadow-white mx-5 my-0 h-4 w-9 animate-third-spin duration-400 origin-center origin-right"
        ></div>
      </div>
      <div>
        <p class="w-full text-xl px-5 text-center text-gray-900">
          {{ text }}
        </p>
      </div>

      <!-- </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomLoader",
  data() {
    return {
      sentences: [
        {
          text: "Loading data, please wait...",
          duration: 0,
        },
        {
          text: "Gathering information...",
          duration: 4,
        },
        {
          text: "Fetching resources...",
          duration: 5,
        },
        {
          text: "Preparing content...",
          duration: 7,
        },
        {
          text: "Almost there! Just a few more seconds...",
          duration: 8,
        },
        {
          text: "Hold on tight, we're almost finished loading!",
          duration: 2,
        },
        {
          text: "We're almost done, hang in there!",
          duration: 3,
        },
        {
          text: "The data is on its way, just a little bit longer...",
          duration: 4,
        },
        {
          text: "Retrieving data, please be patient...",
          duration: 5,
        },
        {
          text: "Just a moment while we load everything up for you...",
          duration: 6,
        },
        {
          text: "We're working hard to get everything ready for you!",
          duration: 7,
        },
        {
          text: "We apologize for the wait, but the data is worth it!",
          duration: 4,
        },
        {
          text: "The data is loading, just a bit more time...",
          duration: 5,
        },
        {
          text: "We're almost done preparing the data, hang in there!",
          duration: 6,
        },
        {
          text: "Please hold while we load the requested information...",
          duration: 7,
        },
        {
          text: "Thanks for your patience while we load the data!",
          duration: 8,
        },
        {
          text: "We're getting everything ready for you, just a little bit longer...",
          duration: 9,
        },
        {
          text: "Just a few more seconds and the data will be ready for you!",
          duration: 1,
        },
        {
          text: "We're almost there, hang tight!",
          duration: 2,
        },
        {
          text: "The data is almost ready, please be patient a little longer...",
          duration: 3,
        },
      ],
      text: "",
    };
  },
  methods: {
    getRandomSentence() {
      const randomIndex = Math.floor(Math.random() * this.sentences.length);
      const randomSentence = this.sentences[randomIndex];
      this.text = randomSentence.text;
      setTimeout(() => {
        this.getRandomSentence();
      }, randomSentence.duration * 200);
    },
  },

  mounted() {
    this.getRandomSentence();
  },
};
</script>

<style>
@keyframes blink {
  50% {
    color: transparent;
  }
}
.blinke-dot {
  animation: 2s blink infinite;
}
.blinke-dot:nth-child(2) {
  animation-delay: 250ms;
}
.blinke-dot:nth-child(3) {
  animation-delay: 500ms;
}

.override-opacity {
  opacity: 0.9 !important;
}
</style>
