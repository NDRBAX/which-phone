import { defineStore } from "pinia";

import axios from "axios";

export const useCheckedStore = defineStore({
  id: "checked",
  state: () => ({
    values: [
      {
        step: null,
        checked: [],
      },
    ],
  }),

  getters: {
    getValuesByStep: (state) => (step) => {
      return state.values[step];
    },
    getAllValues: (state) => {
      return state.values;
    },
  },
  actions: {
    setCheckedByStep(step, checked) {
      // check if step exists
      if (this.values[step]) {
        // remove the step
        this.values.splice(step, 1);
        this.values.splice(step, 0, {
          step: step,
          checked: [checked],
        });
      } else {
        this.values[step] = {
          step: step,
          checked: [checked],
        };
      }
      console.log(this.getAllValues);
    },

    clearStore() {
      this.values = [
        {
          step: null,
          checked: [],
        },
      ];
      console.log("cleared");
      console.log(this.getAllValues);
    },

    async submitNow() {
      let url = "/wphone/submit";
      let user = "Test";
      let values = "test";
      let data = {
        user: user,
        values: values,
      };

      let config = {
        withCredentials: false,
        headers: {
          "Content-Type": "application/json",
        },
      };
      await axios.post(url, data, config).then((response) => {
        console.log(response);
      });
    },
  },
});

export const useDataStore = defineStore({
  id: "data",
  state: () => ({
    data: false,
  }),
  getters: {
    getData: (state) => {
      return state.data;
    },
  },
  actions: {
    setData(data) {
      this.data = data;
    },
  },
});

export const useWishlistStore = defineStore({
  id: "wishlist",
  state: () => ({
    wishlist: [
      {
        device_id: null,
        name: null,
        price: null,
        thumbnail: null,
        summary: null,
        battery: null,
        camera: null,
        screen: null,
        ram: null,
        storage: null,
        selfie: null,
        musicplay: null,
        talktime: null,
        standby: null,
      },
    ],
  }),
  getters: {
    getWishlist: (state) => {
      // remove first element
      state.wishlist.shift();
      return state.wishlist;
    },
    getIdWishlist: (state) => {
      return state.wishlist.map((item) => item.device_id);
    },
  },
  actions: {
    async initializeWishlist() {
      let accessToken = localStorage.getItem("access");
      let refreshToken = localStorage.getItem("refresh");
      let userName = localStorage.getItem("username");
      let CSRFToken = localStorage.getItem("csrfToken");
      console.log(userName);

      if (accessToken && refreshToken && userName) {
        let url = "/wphone/get_wishlist";
        let config = {
          withCredentials: false,
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": CSRFToken,
          },
        };

        await axios
          .get(url, { params: { username: userName } }, config)
          .then((response) => {
            let wishlist = response.data;
            console.log("wishlist", wishlist);
            for (let i = 0; i < wishlist.length; i++) {
              this.editWishlist(
                wishlist[i].id,
                wishlist[i].name,
                wishlist[i].price,
                wishlist[i].thumbnail,
                wishlist[i].summary,
                wishlist[i].battery,
                wishlist[i].rear_camera,
                wishlist[i].secreen_size,
                wishlist[i].ram,
                wishlist[i].storage,
                wishlist[i].front_camera,
                wishlist[i].music_time,
                wishlist[i].talk_time,
                wishlist[i].standby_time
              );
            }
          });

        console.log("wishlist initialized");
      } else {
        this.clearWishlist();
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
      this.wishlist.push({
        device_id: device_id,
        name: name,
        price: price,
        thumbnail: thumbnail,
        summary: summary,
        battery: battery,
        camera: camera,
        screen: screen,
        ram: ram,
        storage: storage,
        selfie: selfie,
        musicplay: musicplay,
        talktime: talktime,
        standby: standby,
      });
    },

    editLocalWishlist(
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
      const wishlist = this.getWishlist;
      const itemIndex = wishlist.findIndex(
        (item) => item.device_id === device_id
      );
      if (itemIndex === -1) {
        this.editWishlist(
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
        console.log("added to wishlist");
      } else {
        this.wishlist.splice(itemIndex, 1);
        console.log("removed from wishlist");
      }
      // update pinia store
      this.wishlist = wishlist;
    },

    removeFromWishlist(device_id) {
      let wishlist = this.getWishlist;
      let index = wishlist.findIndex((item) => item.device_id === device_id);
      this.wishlist.splice(index, 1);
      console.log("removed from wishlist");
    },

    async saveToDB() {
      let accessToken = localStorage.getItem("access");
      let refreshToken = localStorage.getItem("refresh");
      let userName = localStorage.getItem("username");
      let CSRFToken = localStorage.getItem("csrfToken");

      // get all device_id from wishlist
      let wishlist = this.getWishlist;
      let devices_id = wishlist.map((item) => item.device_id);

      console.log("wishlist", devices_id);
      if (accessToken && refreshToken && userName) {
        let url = "/wphone/edit_wishlist";
        let config = {
          withCredentials: false,
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": CSRFToken,
          },
        };

        await axios
          .post(url, { user: userName, devices: devices_id }, config)
          .then((response) => {
            console.log("wishlist saved", response.data);
          });
      }
    },

    clearWishlist() {
      this.wishlist = [
        {
          device_id: null,
          name: null,
          price: null,
          thumbnail: null,
          summary: null,
          battery: null,
          camera: null,
          screen: null,
          ram: null,
          storage: null,
          selfie: null,
          musicplay: null,
          talktime: null,
          standby: null,
        },
      ];
      console.log("wishlist cleared");
    },
  },
});
