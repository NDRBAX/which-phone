<template>
  <!-- HEART ICON -->
  <div class="relative w-full">
    <font-awesome-icon
      :class="[
        $props.inWishlist
          ? 'absolute z-20 right-[-15px] top-[150px] text-2xl duration-300  xs:w-8 xs:w-8 sm:w-8 sm:h-8 text-red-accent-200 hover:text-red-accent-100 cursor-pointer'
          : 'absolute z-20 right-[-15px] top-[150px] text-2xl duration-300 text-gray-400 xs:w-8 xs:w-8 sm:w-8 sm:h-8 hover:text-red-accent-200 cursor-pointer',
      ]"
      icon="fa-solid fa-heart "
      v-on:click="
        editWishlist(
          $props.device_id,
          $props.name,
          $props.price,
          $props.thumbnail,
          $props.summary,
          $props.battery,
          $props.camera,
          $props.screen,
          $props.ram,
          $props.storage,
          $props.selfie,
          $props.musicplay,
          $props.talktime,
          $props.standby
        )
      "
    />
  </div>
  <!-- CARD IMAGE AND DETAIL BUTTON -->
  <div class="group items-center flex justify-center">
    <button
      v-on:click="showDetails"
      id="details"
      class="absolute z-10 items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white bg-transparent hidden group-hover:backdrop-blur-sm bg-white/30 group-hover:block ring-inset ring-2 ring-white group-hover:-translate-y-5 transition duration-300 rounded shadow-md xs:w-auto focus:shadow-outline focus:outline-none"
    >
      Details
    </button>
    <div
      v-bind:style="{ 'background-image': 'url(' + $props.thumbnail + ')' }"
      class="z-0 bg-gray-300 bg-top h-[200px] w-[200px] group-hover:blur-none group-hover:z-0 rounded-lg shadow-md bg-cover duration-300 group-hover:-translate-y-5 justify-center items-center flex"
    ></div>
  </div>
  <!-- FRONT FACE -->
  <div
    class="front-card min-w-[220px] z-10 lg xl bg-white -mt-10 shadow-lg rounded-lg overflow-hidden"
  >
    <!-- DEVICE -->
    <div
      class="py-5 sm:text-sm md:text-md lg:text-lg xl:text-xl text-center font-bold uppercase tracking-wide text-gray-800"
    >
      {{ $props.name }}
    </div>
    <div class="seperator gradient xs:mb-0 mb-4"></div>

    <Transition>
      <div
        class="relative w-full min-h-[190px] xs:text-xs sm:text-sm md:text-md text-center tracking-wide text-gray-800"
      >
        <!-- SUMMARY -->
        <div v-if="!showBackCard" class="py-5 px-5">
          {{ $props.summary }}
        </div>
        <!-- DETAILS -->
        <div v-if="showBackCard" class="h-full w-full py-5 px-5">
          <table class="w-full">
            <tbody>
              <tr v-if="$props.battery">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-battery-three-quarters"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">Battery {{ $props.battery }} mAh</td>
              </tr>
              <tr v-if="hasStorage">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-hard-drive"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">{{ available_storage }}GB Storage</td>
              </tr>
              <tr v-if="hasRam">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-memory"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">{{ available_ram }}GB RAM</td>
              </tr>
              <tr v-if="hasCamera">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-camera"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">Main Camera {{ $props.camera }}MP</td>
              </tr>
              <tr v-if="hasSelfie">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-image-portrait"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">Selfie Camera {{ $props.selfie }}MP</td>
              </tr>
              <tr v-if="$props.screen">
                <td>
                  <font-awesome-icon
                    icon="fa-solid fa-mobile-screen-button"
                    class="text-xl mr-2"
                  />
                </td>
                <td class="text-start">{{ $props.screen }}" Screen</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </Transition>

    <!-- STORES -->
    <form v-on:submit.prevent="goToMarket">
      <div class="flex">
        <!-- AMAZON -->
        <div
          class="group w-1/3 h-12 flex bg-gray-100 items-center justify-center hover:bg-[#FF9900]"
        >
          <input
            :id="$props.name + 'amazon'"
            type="radio"
            class="peer sr-only"
            :value="[$props.name, 'amazon']"
            name="market"
            v-model="market"
          />
          <label
            :for="$props.name + 'amazon'"
            class="duration-300 cursor-pointer peer-checked:fill-[#FF9900]"
            ><AmazonIcon
              size="25pem"
              class="custom-class duration-300 group-hover:fill-white"
            ></AmazonIcon
          ></label>
        </div>
        <!-- EBAY -->
        <div
          class="group w-1/3 bg-gray-200 h-12 flex items-center justify-center duration-300 hover:bg-[#0064D2]"
        >
          <input
            :id="$props.name + 'ebay'"
            type="radio"
            class="peer sr-only"
            :value="[$props.name, 'ebay']"
            name="market"
            v-model="market"
          />
          <label
            :for="$props.name + 'ebay'"
            class="cursor-pointer peer-checked:fill-[#0064D2]"
            ><EbayIcon
              size="35pem"
              class="custom-class duration-300 group-hover:fill-white"
            ></EbayIcon
          ></label>
        </div>
        <!-- RAKUTEN -->
        <div
          class="group w-1/3 bg-gray-100 h-12 flex items-center justify-center duration-300 hover:bg-[#E31837]"
        >
          <input
            :id="$props.name + 'rakuten'"
            type="radio"
            class="peer sr-only"
            :value="[$props.name, 'rakuten']"
            name="market"
            v-model="market"
          />
          <label
            :for="$props.name + 'rakuten'"
            class="cursor-pointer peer-checked:fill-[#E31837]"
            ><RakutenIcon
              size="25pem"
              class="custom-class duration-300 group-hover:fill-white"
            ></RakutenIcon
          ></label>
        </div>
      </div>
      <!-- PRICE -->
      <div class="flex items-center justify-between py-5 px-6 bg-gray-50">
        <h1
          class="text-gray-800 xs:text-sm sm:text-md md:text-lg lg:text-xl xl:text-2xl font-bold"
        >
          $ {{ price }}
        </h1>

        <button
          type="submit"
          class="xs:text-xs sm:text-sm md:text-md lg:text-lg xl:text-xl px-2 py-1 font-semibold rounded text-white transition duration-200 rounded shadow-md md:w-auto bg-teal-accent-400 enabled:hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none"
        >
          Buy
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { AmazonIcon, RakutenIcon, EbayIcon } from "vue3-simple-icons";
import { useCheckedStore, useWishlistStore } from "../stores/checked";
import { useAuthStore } from "../stores/auth";
// import { ref } from "vue";
export default {
  components: {
    AmazonIcon,
    EbayIcon,
    RakutenIcon,
  },
  data() {
    return {
      showBackCard: false,
      store: useCheckedStore(),
      authStore: useAuthStore(),
      wishlistStore: useWishlistStore(),
      available_ram: this.extractNumbers(this.ram),
      available_storage: this.extractNumbers(this.storage),
      market: "",
    };
  },
  props: {
    name: {
      type: String,
      required: true,
    },
    summary: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
    thumbnail: {
      type: String,
      required: true,
    },
    battery: {
      type: Number,
      required: true,
    },
    storage: {
      type: Array,
      required: true,
    },
    ram: {
      type: Array,
      required: true,
    },
    camera: {
      type: Number || null,
      required: false,
    },
    screen: {
      type: Number || null,
      required: false,
    },
    selfie: {
      type: Number || null,
      required: false,
    },
    standby: {
      type: String,
      required: false,
    },
    talktime: {
      type: String,
      required: false,
    },
    musicplay: {
      type: String,
      required: false,
    },
    device_id: {
      type: String,
      required: true,
    },
    inWishlist: {
      type: Boolean,
      required: false,
    },
  },
  computed: {
    hasRam() {
      if (this.ram !== null) {
        console.log("ram is not null", this.ram);
        return true;
      } else {
        console.log("ram is null");
        return false;
      }
    },
    hasStorage() {
      if (this.storage !== null) {
        console.log("storage is not null");
        return true;
      } else {
        console.log("storage is null");
        return false;
      }
    },
    hasSelfie() {
      if (this.selfie !== null) {
        console.log("selfie is not null");
        return this.selfie;
      } else {
        console.log("selfie is null");
        return false;
      }
    },
    hasCamera() {
      if (this.camera !== null) {
        console.log("camera is not null", this.camera);
        return this.camera;
      } else {
        console.log("camera is null");
        return false;
      }
    },
    isAuthentificated() {
      return this.authStore.access;
    },
  },

  methods: {
    showDetails() {
      this.showBackCard = !this.showBackCard;
    },
    extractNumbers(arr) {
      if (arr.length === 1) {
        return arr[0];
      } else if (arr.length === 2) {
        return arr[0] + " or " + arr[1];
      } else if (arr.length === 3) {
        return arr[0] + ", " + arr[1] + " or " + arr[2];
      } else if (arr.length === 4) {
        return arr[0] + ", " + arr[1] + ", " + arr[2] + " or " + arr[3];
      } else if (arr.length === 5) {
        return (
          arr[0] +
          ", " +
          arr[1] +
          ", " +
          arr[2] +
          ", " +
          arr[3] +
          " or " +
          arr[4]
        );
      } else {
        // Add a default case for arrays with more than 5 elements
        return "Too many numbers to extract!";
      }
    },

    editWishlist(
      device_id,
      name,
      price,
      thumbnail,
      summary,
      battery,
      camera,
      screen,
      ram,
      storage,
      selfie,
      musicplay,
      talktime,
      standby
    ) {
      if (this.isAuthentificated) {
        this.wishlistStore.editLocalWishlist(
          device_id,
          name,
          price,
          thumbnail,
          summary,
          battery,
          camera,
          screen,
          ram,
          storage,
          selfie,
          musicplay,
          talktime,
          standby
        );
      }
    },

    goToMarket() {
      if (this.market[1] === "amazon") {
        window.open(
          "https://www.amazon.com/s?k=" + this.market[0] + "&ref=nb_sb_noss_2",
          "_blank"
        );
      } else if (this.market[1] === "ebay") {
        window.open(
          "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=" +
            this.market[0] +
            "&_sacat=0",
          "_blank"
        );
      } else if (this.market[1] === "rakuten") {
        window.open(
          "https://www.fr.shopping.rakuten.com/search/" + this.market[0],
          "_blank"
        );
      }
    },
  },
};
</script>

<style>
.seperator {
  height: 7px;
  -webkit-animation: animation 10s infinite linear;
  -moz-animation: animation 10s infinite linear;
  animation: animation 10s ease infinite;
}

@-webkit-keyframes animation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@-moz-keyframes animation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@keyframes animation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.gradient {
  background: -webkit-linear-gradient(
    left,
    #a7ffeb 0%,
    #64ffda 50%,
    #1de9b6 100% /*  #1dd1a1 100%  #00bfa5 100% */
  );
  background-size: 400% 400%;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

td {
  height: 30px;
}
</style>
