import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import ArticleList from '@/components/forum/ArticleList'
import Article from '@/components/forum/Article'
import NewArticle from '@/components/forum/NewArticle'
import GifList from '@/components/gif/GifList'
import Gif from '@/components/gif/Gif'
import Auth from '@/components/login/Auth'
import Profile from '@/components/login/Profile'
import Pair from '@/components/Pair'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Pair',
      name: 'Pair',
      component: Pair
    },
    
    {
      path: '/Forum',
      name: 'ArticleList',
      component: ArticleList
    },
    {
      path: '/Forum/new',
      name: 'NewArticle',
      component: NewArticle
    },
    {
      path: '/Forum/id/:id',
      name: 'Article',
      component: Article,
      props: true
    },
    {
      path: '/Gif',
      name: 'GifList',
      component: GifList
    },
    {
      path: '/Gif/:id',
      name: 'Gif',
      component: Gif,
      props: true
    },
    {
      path: '/Auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile
    }
  ]
})
