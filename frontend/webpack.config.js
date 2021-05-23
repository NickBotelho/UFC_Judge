const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const isProduction =
    process.argv[process.argv.indexOf("--mode") + 1] === "production";
module.exports = {
    devServer: {
        historyApiFallback: true,
        proxy: {
            "/api": {
                target: "http://localhost:5100",
                pathRewrite: { "^/api$": "" },
                changeOrigin: true,
            },
        },
    },
    entry: {
        main: ["babel-polyfill", path.join(__dirname, "src", "index.js")],
    },
    output: {
        path: path.join(__dirname, "server/", "build/"),
        // publicPath: isProduction ? "/build/" : "/",
        filename: "main.js",
    },
    optimization: {
        removeAvailableModules: false,
        removeEmptyChunks: false,
        splitChunks: false,
    },
    resolve: {
        alias: {

        },
    },
    module: {
        rules: [
            {
                test: /.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                },
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.svg$/,
                use: ["@svgr/webpack"],
            },
            {
                test: /\.ttf$/,
                use: [
                    {
                        loader: "ttf-loader",
                        options: {
                            name: "./font/[hash].[ext]",
                        },
                    },
                ],
            },
            {
                test: /\.(png|woff|woff2|eot)$/,
                loader: "file-loader",
            },
        ],
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: "index.html",
            template: path.join(__dirname, "src", "index.html"),
        }),
    ],
};