import {createApi} from "@reduxjs/toolkit/query/react";
import type { ICategoryItem } from "./types";
import {createBaseQuery} from "../utils/createBaseQuery.ts";

export const apiCategory = createApi({
   reducerPath: 'api',
   baseQuery: createBaseQuery("categories"),
   endpoints: (builder) => ({
      getCategories:  builder.query<ICategoryItem[], void>({
         query: () => ''
      }),
   })
    
});


export const {
   useGetCategoriesQuery
} = apiCategory;