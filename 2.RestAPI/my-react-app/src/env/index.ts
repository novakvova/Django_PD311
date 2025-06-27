const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const APP_GOOGLE_OAUTH = import.meta.env.VITE_APP_GOOGLE_OAUTH;
// const APP_IMAGE_URL = API_BASE_URL + import.meta.env.VITE_APP_IMAGE_URL;

// const IMAGES_50_URL = APP_IMAGE_URL + '/50_';
// const IMAGES_100_URL = APP_IMAGE_URL + '/100_';
// const IMAGES_200_URL = APP_IMAGE_URL + '/200_';
// const IMAGES_400_URL = APP_IMAGE_URL + '/400_';
// const IMAGES_800_URL = APP_IMAGE_URL + '/800_';
// const IMAGES_1200_URL = APP_IMAGE_URL + '/1200_';

const APP_ENV = {
    API_BASE_URL,
    APP_GOOGLE_OAUTH,
    // IMAGES_50_URL,
    // IMAGES_100_URL,
    // IMAGES_200_URL,
    // IMAGES_400_URL,
    // IMAGES_800_URL,
    // IMAGES_1200_URL,
}

export { APP_ENV };