import { PassportStatic } from 'passport'
import { Strategy as BnetStrategy } from 'passport-bnet'

export default (passport: PassportStatic) => {
    passport.use(new BnetStrategy({
        clientID: 'b3bb0ce94dfb433b9265c458deabb736',
        clientSecret: 'Yrkrv2wviRmZwla9hgURwkNi8bZfR1SZ',
        callbackURL: "https://localhost:3000/oauth/battlenet/callback",
        region: "us"
    }, function(accessToken, refreshToken, profile, done) {
        return done(null, profile);
    }));
}



