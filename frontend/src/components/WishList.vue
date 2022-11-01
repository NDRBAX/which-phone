<template>
  <div class="center grid">
    <vs-row>
      <vs-col
        :key="index"
        v-for="(col, index) in 3"
        vs-type="flex"
        vs-justify="center"
        vs-align="center"
        w="3"
      >
        <div v-for="item in wishlist" :key="item.id">
          <vs-card type="5">
            <template #title>
              <h3>{{ item.name }}</h3>
            </template>
            <template #img>
              <img :src="item.image" alt="" />
            </template>
            <template #text>
              <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit.</p>
            </template>
            <template #interactions>
              <vs-button danger icon>
                <i class="bx bx-heart"></i>
              </vs-button>
              <vs-button class="btn-chat" shadow primary>
                <i class="bx bx-chat"></i>
                <span class="span"> ${{ item.price }} </span>
              </vs-button>
            </template>
          </vs-card>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  mounted() {
    axios.get("http://127.0.0.1:8000/api/wishlist/").then((response) => {
      this.wishlist = response.data;
      console.log(response.data);
    });
  },
  name: "WishList",
  data: () => ({
    wishlist: [],
  }),
};
</script>
