import express, { Application, Error, Request, Response, NextFunction } from 'express'
import passport from 'passport'
import * as defaultConfig from './defaultConfig'
import loadPassport from './passport'



class App {
    private config: any;
    private app: Application;

    constructor(config?: any) {
        this.app = express();
        this.config = {
            ...defaultConfig,
            ...config
        }

        this.configure();
    }

    listen = (port: number = this.config.port, host: string = this.config.host) {}

    private configure (app: Application = this.app, config: any = this.config) {
        loadPassport(passport)

        app.use(passport.initialize());
        app.use(passport.session());
        app.use(config.mountPoint, mainRouter)

        app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
            next()
        })
    }
}
export default App