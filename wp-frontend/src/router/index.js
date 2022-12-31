import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import SearchView from "../views/SearchView.vue";
import ProfileView from "../views/ProfileView.vue";
import WishListView from "../views/WishListView.vue";
import CategoriesView from "../views/CategoriesView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",

      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/settings",
      name: "profile",

      component: ProfileView,
    },
    {
      path: "/wishlist",
      name: "wishlist",
      component: WishListView,
    },
    {
      path: "/categories",
      name: "categories",
      component: CategoriesView,
    },
  ],
});

export default router;
