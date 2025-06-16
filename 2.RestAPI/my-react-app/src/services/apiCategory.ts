import {createApi, fetchBaseQuery} from "@reduxjs/toolkit/query/react";
import type { ICategoryItem } from "./types";

export const apiCategory = createApi({
   reducerPath: 'api',
   baseQuery: fetchBaseQuery({baseUrl: 'http://127.0.0.1:4096/api/'}),
   endpoints: (builder) => ({
      getCategories:  builder.query<ICategoryItem[], void>({
         query: () => 'categories' 
      }),
   })
    
});


export const {
   useGetCategoriesQuery
} = apiCategory;